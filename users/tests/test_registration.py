from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from users.models import CustomUser
from users.views import StudentRegistration, TeacherRegistration


class RegistrationTests(APITestCase):
    """
    Test class for registration functionality.
    """
    def register_teacher(self, email, password, first_name, last_name):
        """
        Registers a teacher via post request to the registration url.
        """
        url = reverse(TeacherRegistration.name)
        data = {
            'email': email,
            'password': password,
            'first_name': first_name,
            'last_name': last_name
        }
        response = self.client.post(url, data, format='json')
        return response

    def register_student(self, email, password, first_name, last_name, year):
        """
        Registers a student via post request to the registration url.
        """
        url = reverse(StudentRegistration.name)
        data = {
            'email': email,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
            'year': year
        }
        response = self.client.post(url, data, format='json')
        return response

    def test_teacher_registration(self):
        """
        Ensure that the registration is successful and it creates CustomUser with
        is_teacher filed set to True
        """
        email = 'test_email@mail.com'
        password = 'test_password'
        first_name = 'test_first_name'
        last_name = 'test_last_name'
        response = self.register_teacher(email, password, first_name, last_name)
        assert response.status_code == status.HTTP_201_CREATED
        assert CustomUser.objects.count() == 1

        teacher = CustomUser.objects.get()
        assert teacher.email == email
        assert teacher.first_name == first_name
        assert teacher.last_name == last_name
        assert teacher.is_teacher is True

    def test_student_registration(self):
        """
        Ensure that the registration is successful and it creates CustomUser with
        is_teacher filed set to False
        """
        email = 'test_email_s@mail.com'
        password = 'test_password_s'
        first_name = 'test_first_name_s'
        last_name = 'test_last_name_s'
        year = 2
        response = self.register_student(email, password, first_name, last_name, year)

        assert response.status_code == status.HTTP_201_CREATED
        assert CustomUser.objects.count() == 1

        student = CustomUser.objects.get()
        assert student.email == email
        assert student.first_name == first_name
        assert student.last_name == last_name
        assert student.is_teacher is False

    def test_registration_with_already_registered_email(self):
        """
        Ensure that user cannot register with already registered email
        """
        email = 'test_email_s@mail.com'
        password = 'test_password_s'
        first_name = 'test_first_name_s'
        last_name = 'test_last_name_s'
        year = 2
        response = self.register_student(email, password, first_name, last_name, year)

        assert response.status_code == status.HTTP_201_CREATED
        assert CustomUser.objects.count() == 1

        response = self.register_student(email, password, first_name, last_name, year)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['email'][0] == 'custom user with this email already exists.'