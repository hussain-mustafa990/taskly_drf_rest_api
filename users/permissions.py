from rest_framework import permissions

class IsUserOwnerOrGetAndPostOnly(permissions.BasePermission):
    """
    Custom permissions for UserViewSet to only allow user to edit their own user. Othwerwise, Get and Post Only.
    """

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user.is_anonymous:
            return request.user == obj

        return False

class IsProfileOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permissions for ProfileViewSet to only allow user to edit their own profile. Othwerwise, Get and Post Only.
    """

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not request.user.is_anonymous:
            return request.user.profile == obj
        
        return False
