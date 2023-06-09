from rest_framework import permissions
from .models import User
from rest_framework.views import View


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return request.user.is_superuser or obj == request.user


class IsColaborator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff or request.user.is_superuser


class IsStudentAble(permissions.BasePermission):
    def has_object_permission(self, request, view):
        return request.user.is_blocked
