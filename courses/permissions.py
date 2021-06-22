from rest_framework import permissions


class IsCourseYearAllowed(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.year == request.user.year


class IsTeacherOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_teacher
