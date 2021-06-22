from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import CustomUser
from .serializers import StudentRegistrationSerializer, TeacherRegistrationSerializer


class Login(ObtainAuthToken):
    """
    Return token of a user.
    """
    name = 'login'

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key
        })


class Logout(generics.CreateAPIView):
    """
    Delete token of a request's user.
    """
    permission_classes = IsAuthenticated
    name = 'logout'

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class StudentRegistration(generics.CreateAPIView):
    """
    Register new student
    """
    queryset = CustomUser.objects.all()
    serializer_class = StudentRegistrationSerializer
    name = 'registration-student'


class TeacherRegistration(generics.CreateAPIView):
    """
    Register new teacher
    """
    queryset = CustomUser.objects.all()
    serializer_class = TeacherRegistrationSerializer
    name = 'registration-teacher'


class ApiRoot(generics.GenericAPIView):
    """
    Return a list of available endpoints.
    """
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'students registration': reverse(StudentRegistration.name, request=request),
            'teachers registration': reverse(TeacherRegistration.name, request=request),
            'login': reverse(Login.name, request=request),
            'logout': reverse(Logout.name, request=request),
            })
