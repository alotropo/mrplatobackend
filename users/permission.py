from rest_framework.permissions import BasePermission,SAFE_METHODS


class CustomPermition(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS and request.user.is_superuser:
            return True
        return obj == request.user

