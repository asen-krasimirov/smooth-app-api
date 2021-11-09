# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
# from rest_framework import permissions
# from tutorial.quickstart.serializers import UserSerializer, GroupSerializer
from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, RetrieveAPIView
from smooth_api.smooth_auth.serializers import SmoothUserSerializer

UserModel = get_user_model()


class SmoothUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    # queryset = User.objects.all().order_by('-date_joined')
    queryset = UserModel.objects.all()
    serializer_class = SmoothUserSerializer
    # permission_classes = [permissions.IsAuthenticated]


# from django.contrib.auth.models import User


class UserList(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = SmoothUserSerializer


class UserDetail(RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = SmoothUserSerializer
