from django.urls import path

from users.views import ApiRoot, Login, Logout, StudentRegistration, TeacherRegistration

urlpatterns = [
    path('', ApiRoot.as_view(), name=ApiRoot.name),
    path('registration/teacher/', TeacherRegistration.as_view(), name=TeacherRegistration.name),
    path('registration/student/', StudentRegistration.as_view(), name=StudentRegistration.name),
    path('login/', Login.as_view(), name=Login.name),
    path('logout/', Logout.as_view(), name=Logout.name),
]