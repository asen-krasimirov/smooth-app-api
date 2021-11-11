from django.contrib.auth.models import User
from knox.models import AuthToken
from rest_framework import authentication
from rest_framework import exceptions
from smooth_api.smooth_auth.models import SmoothSession


# class Authentication(authentication.BaseAuthentication):
#     def authenticate(self, request):
#         # key = request.META.get('AUTH_TOKEN')
#         key = request.query_params.get('AUTH_TOKEN')
#         if not key:
#             return None
#
#         try:
#             # token = AuthToken.objects.get(key=key)
#             user = SmoothSession.objects.get(token=key).user
#         except User.DoesNotExist:
#             raise exceptions.AuthenticationFailed('Not authenticated!')
#
#         return user, None
