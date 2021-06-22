from django.db.models import Q

from rest_framework import generics

from .models import Course
from .serializers import CourseSerializer


class CourseCreation(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    name = 'creation-course'


class AllCourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    name = 'list-course-all'


class PersonalCourseList(generics.ListAPIView):
    serializer_class = CourseSerializer
    name = 'list-course-personal'

    def get_queryset(self):
        user = self.request.user
        return Course.objects.filter(Q(instructor=user) | Q(participants=user))
