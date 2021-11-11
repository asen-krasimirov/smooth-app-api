# from django.contrib.auth.models import User, Group
# from rest_framework import permissions
# from tutorial.quickstart.serializers import UserSerializer, GroupSerializer

from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.urls import reverse

from knox.models import AuthToken

from rest_framework import viewsets, response, status
from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.response import Response
from smooth_api.smooth_auth.models import SmoothSession

from smooth_api.smooth_auth.serializers import RegisterSerializer, LoginSerializer
from smooth_api.smooth_auth.serializers import SmoothUserSerializer

# , LoginUserSerializer

# RegisterUserSerializer, LoginUserSerializer

UserModel = get_user_model()


class SmoothUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    # queryset = User.objects.all().order_by('-date_joined')
    queryset = UserModel.objects.all()
    serializer_class = SmoothUserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class UserList(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = SmoothUserSerializer


class UserDetail(RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = SmoothUserSerializer


def make_live_session(user):
    token = AuthToken.objects.create(user)[1]

    SmoothSession.objects.create(
        user=user,
        token=token
    )

    return token


class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=self.request.data)

        if serializer.is_valid():
            user = serializer.save()

            token = make_live_session(user)

            return Response({
                "user": SmoothUserSerializer(user, context=self.get_serializer_context()).data,
                "token": token
            })

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=self.request.data)

        if serializer.is_valid():
            user = serializer.validated_data

            token = make_live_session(user)

            return Response({
                "user": SmoothUserSerializer(user, context=self.get_serializer_context()).data,
                "token": token
            })

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
