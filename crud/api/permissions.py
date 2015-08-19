from rest_framework import permissions


class IsOwnerOrSuperReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        # Only return True if the chirp is the same as the user
        return (obj.owner == request.user or obj.owner == request.user.is_superuser)
