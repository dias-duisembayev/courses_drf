from django.db.models import Q

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Course
from .permissions import IsCourseYearAllowed, IsCourseTeacherOrReadOnly
from .serializers import CourseSerializer
from users.permissions import IsStudent, IsTeacher


class CourseCreation(generics.CreateAPIView):
    """
    Create new course.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsTeacher]
    name = 'course-creation'


class AllCourseList(generics.ListAPIView):
    """
    List all courses.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated,]
    name = 'course-all-list'
    filter_fields = (
        'year',
    )
    ordering_fields = (
        'name',
        'abbr',
        'capacity',
    )


class PersonalCourseList(generics.ListAPIView):
    """
    List courses where request.user is either a participant or an instructor.
    """
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated,]
    name = 'course-personal-list'
    ordering_fields = (
        'name',
        'abbr',
        'capacity',
    )

    def get_queryset(self):
        """
        Returns courses where request.user is either a participant or an instructor
        """
        user = self.request.user
        return Course.objects.filter(Q(instructor=user) | Q(participants=user))


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, put, delete a single course.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsCourseTeacherOrReadOnly]
    name = 'course-detail'


class CourseAddition(generics.UpdateAPIView):
    """
    Adds request.user to the set of participants of the course.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsStudent, IsCourseYearAllowed]
    name = 'course-addition'

    def update(self, request, *args, **kwargs):
        course = self.get_object()
        participant = self.request.user
        course.participants.add(participant)
        course.capacity = course.capacity+1
        course.save()
        serializer = self.get_serializer(course)
        return Response(serializer.data)
