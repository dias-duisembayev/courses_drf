from django.urls import path

from courses.views import CourseCreation, AllCourseList, PersonalCourseList

urlpatterns = [
    path('create/', CourseCreation.as_view(), name=CourseCreation.name),
    path('all/', AllCourseList.as_view(), name=AllCourseList.name),
    path('my/', PersonalCourseList.as_view(), name=PersonalCourseList.name),
]
