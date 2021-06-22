from rest_framework import permissions


class IsTeacher(permissions.BasePermission):
    """
    Permission class for identifying a teacher.
    """
    def has_permission(self, request, view):
        """
        Return true if request.user is a teacher (is_teacher boolean field is set to True).
        """
        return request.user.is_teacher


class IsStudent(permissions.BasePermission):
    """
    Permission class for identifying a student.
    """
    def has_permission(self, request, view):
        """
        Return true if request.user is a student (is_teacher boolean field is set to False).
        """
        return not request.user.is_teacher
