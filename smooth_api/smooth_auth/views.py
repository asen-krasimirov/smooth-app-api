import datetime

from django.contrib.auth import get_user_model
from rest_framework import viewsets, status, exceptions
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.response import Response
from smooth_api.core.tasks import generate_token
from smooth_api.smooth_auth.models import SmoothSession, SmoothUser, BusinessProfile, ApplicantProfile
from smooth_api.smooth_auth.serializers import RegisterSerializer, LoginSerializer, BusinessProfileSerializer, \
    ApplicantProfileSerializer
from smooth_api.smooth_auth.serializers import SmoothUserSerializer

UserModel = get_user_model()


# class SmoothUserViewSet(viewsets.ModelViewSet):
#     queryset = UserModel.objects.all()
#     serializer_class = SmoothUserSerializer


class UserList(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = SmoothUserSerializer


class UserDetail(RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = SmoothUserSerializer


def make_live_session(user):
    token = generate_token(64)

    expiry_date = datetime.datetime.now() + datetime.timedelta(days=7)

    SmoothSession.objects.create(
        user=user,
        token=token,
        expiry_data=expiry_date
    )

    return token


def is_logged(user):
    session = SmoothSession.objects.filter(user=user).first()
    if session and not session.has_expired():
        return session.token


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=self.request.data)

        if serializer.is_valid():
            user = serializer.save()

            token = make_live_session(user)

            return Response({
                'user': SmoothUserSerializer(user, context=self.get_serializer_context()).data,
                'token': token
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=self.request.data)

        if serializer.is_valid():
            user = serializer.validated_data

            token = is_logged(user)
            if not token:
                token = make_live_session(user)

            return Response({
                'user': SmoothUserSerializer(user, context=self.get_serializer_context()).data,
                'token': token
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(GenericAPIView):

    def post(self, request):
        key = request.query_params.get('AUTH_TOKEN')

        try:
            session = SmoothSession.objects.get(
                token=key
            )

            session.delete()
        except:
            raise exceptions.AuthenticationFailed({'error_message': 'Not Authorized!'})

        return Response({
            'message': 'Successfully logged out!'
        })


class ProfileDetails(GenericAPIView):

    def get(self, request, *args, **kwargs):
        user_pk = kwargs.get('user_id')
        try:
            user = SmoothUser.objects.filter(
                pk=user_pk
            ).first()

            if not user:
                raise ValidationError({'error_message': 'User not found!'})

            if user.is_business:
                profile = BusinessProfile.objects.get(
                    pk=user_pk
                )

                self.serializer_class = BusinessProfileSerializer

                profile = BusinessProfileSerializer(profile, context=self.get_serializer_context()).data,

            else:
                profile = ApplicantProfile.objects.get(
                    pk=user_pk
                )

                self.serializer_class = BusinessProfileSerializer

                profile = ApplicantProfileSerializer(profile, context=self.get_serializer_context()).data,

        except Exception as e:
            raise ValidationError({'error_message': e})

        return Response(profile[0])

    def put(self, request, *args, **kwargs):
        token = request.query_params.get('AUTH_TOKEN')
        user_pk = kwargs.get('user_id')
        current_user = SmoothSession.objects.filter(
            token=token,
        ).first()

        if not current_user:
            raise ValidationError({'error_message': 'Not Authenticated or Not Authorized!'})

        user = SmoothUser.objects.filter(
            pk=user_pk
        ).first()

        if not user:
            raise ValidationError({'error_message': 'User not found!'})

        if user.pk != current_user.pk:
            raise ValidationError({'error_message': 'Not Authorized!'})

        is_business = user.is_business

        try:
            if is_business:
                profile = BusinessProfile.objects.get(
                    pk=user_pk
                )

                self.serializer_class = BusinessProfileSerializer

            else:
                profile = ApplicantProfile.objects.get(
                    pk=user_pk
                )

                self.serializer_class = ApplicantProfileSerializer

            data = dict(request.data)
            if not is_business:
                data['education'] = data['education'].split(';')
                data['skills'] = data['skills'].split(';')

            profile_serialized = self.serializer_class(data=data)
            if profile_serialized.is_valid():
                profile_serialized = profile_serialized.update(profile, profile_serialized.validated_data)
            else:
                raise ValidationError({'error_message': 'Put valid data!'})

            profile = self.serializer_class(profile_serialized, context=self.get_serializer_context()).data,

        except Exception as e:
            raise ValidationError(e.args[0])

        return Response(profile[0])
