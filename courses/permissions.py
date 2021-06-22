from rest_framework import permissions


class IsCourseYearAllowed(permissions.BasePermission):
    """
    Permission class for identifying if a course's year is the same as student's.
    """
    def has_object_permission(self, request, view, obj):
        """
        Return true if request.user's year field equals to the course's(obj) year field.
        """
        return obj.year == request.user.year


class IsCourseTeacherOrReadOnly(permissions.BasePermission):
    """
    Permission class for identifying if user is a teacher or if a action is safe.
    """
    def has_object_permission(self, request, view, obj):
        """
        Return true if the action is safe or if request.user is a teacher.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.instructor == request.user
