from django.urls import path

from courses.views import CourseCreation, AllCourseList, PersonalCourseList, CourseDetail, CourseAddition

urlpatterns = [
    path('create/', CourseCreation.as_view(), name=CourseCreation.name),
    path('all/', AllCourseList.as_view(), name=AllCourseList.name),
    path('my/', PersonalCourseList.as_view(), name=PersonalCourseList.name),
    path('<pk>/', CourseDetail.as_view(), name=CourseDetail.name),
    path('<pk>/enroll/', CourseAddition.as_view(), name=CourseAddition.name),
]
