from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    '''Права на изменения только автору либо только просмотр'''
    def has_object_permission(self, request, _view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)


class ReadOnly(permissions.BasePermission):
    '''Права только на просмотр'''
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_admin or request.user.is_superuser)
