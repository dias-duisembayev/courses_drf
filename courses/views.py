from django.db.models import Q

from rest_framework import generics
from rest_framework.response import Response

from .models import Course
from .serializers import CourseSerializer


class CourseCreation(generics.CreateAPIView):
    """
    Create new course
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    name = 'course-creation'


class AllCourseList(generics.ListAPIView):
    """
    List all courses
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    name = 'course-all-list'


class PersonalCourseList(generics.ListAPIView):
    """
    List courses where request.user is either a participant or an instructor
    """
    serializer_class = CourseSerializer
    name = 'course-personal-list'

    def get_queryset(self):
        """
        Returns courses where request.user is either a participant or an instructor
        """
        user = self.request.user
        return Course.objects.filter(Q(instructor=user) | Q(participants=user))


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, put, delete a single course
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    name = 'course-detail'


class CourseAddition(generics.UpdateAPIView):
    """
    Adds request.user to the set of participants of the course
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    name = 'course-addition'

    def update(self, request, *args, **kwargs):
        course = self.get_object()
        participant = self.request.user
        course.participants.add(participant)
        course.save()
        serializer = self.get_serializer(course)
        return Response(serializer.data)
