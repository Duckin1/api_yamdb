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

class AdminOnlyPermission(permissions.BasePermission):
    '''Права доступа строго только администратора.'''

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.user.is_authenticated and request.user.is_admin:
            return True