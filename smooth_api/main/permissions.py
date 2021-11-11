from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    pass
#     """
#     Custom permission to only allow owners of an object to edit it.
#     """
#
#     def has_object_permission(self, request, view, obj):
#         # Allowing only GET, HEAD or OPTIONS requests to all users.
#         if request.method in permissions.SAFE_METHODS:
#             return True
#
#         return obj.owner == request.user
