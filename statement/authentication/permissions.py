from rest_framework import permissions


class DjangoModelPermissionsOrAnonReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
        #return super().has_object_permission(request, view, obj)
            return True
        #return obj.user == request.user