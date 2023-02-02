from rest_framework import permissions


def check_post(request):
    return (request.method == 'POST'
            and (request.user.is_user
                 or request.user.is_moderator
                 or request.user.is_admin))


def check_patch_delete(request, obj):
    methods = ['PATCH', 'DELETE']
    return (request.method in methods
            and (request.user.is_admin
                 or request.user.is_moderator
                 or request.user == obj.author))


class IsAuthorOrReadOnly(permissions.BasePermission):
    '''Права на изменения только автору либо только просмотр'''

    def has_object_permission(self, request, _view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)


class IsAdminSafeMethods(permissions.BasePermission):
    """Права доступа для администратора, супрюзера и при безопасных методах"""

    def has_permission(self, request, view):
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_superuser
                or request.user.is_authenticated and request.user.is_admin
        )


class ReviewAndCommentsPermissions(permissions.BasePermission):
    """Проверка прав доступа для ревью и комментариев"""

    def has_permission(self, request, view):
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_superuser
                or request.user.is_admin
                or request.user.is_moderator
                or request.user == obj.author
        )


class AdminOnlyPermission(permissions.BasePermission):
    """Права доступа строго только администратора."""

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.user.is_authenticated and request.user.is_admin:
            return True


class AdminOrReadOnly(permissions.BasePermission):
    '''Только администратор или чтение.'''

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
                and (request.user.is_superuser or request.user.is_admin))


class StaffOrAuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_superuser
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_superuser
                or (request.user.is_authenticated
                    and (check_patch_delete(request, obj)
                         or check_post(request))))
