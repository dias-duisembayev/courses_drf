from django.urls import reverse

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from users.models import CustomUser
from users.views import Login, Logout


class AuthenticationTests(APITestCase):
    """
    Test class for login/logout functionality.
    """
    def create_user(self, email, password, first_name, last_name):
        """
        Create new CustomUser for testing
        """
        user = CustomUser.objects.create_user(email, first_name, last_name, False, password)
        return user

    def test_user_login(self):
        """
        Ensure that the user can login and get token
        """
        email = 'test_email@mail.com'
        password = 'test_password'
        first_name = 'test_first_name'
        last_name = 'test_last_name'
        user = self.create_user(email, password, first_name, last_name)
        token = Token.objects.create(user=user)
        url = reverse(Login.name)
        data = {
            'username': email,
            'password': password,
        }
        response = self.client.post(url, data, format='json')
        assert response.data['token'] == token.key
        assert response.status_code == status.HTTP_200_OK

    def test_user_login_wrong_password(self):
        """
        Ensure that the user can login and get token
        """
        email = 'test_email@mail.com'
        password = 'test_password'
        first_name = 'test_first_name'
        last_name = 'test_last_name'
        user = self.create_user(email, password, first_name, last_name)
        token = Token.objects.create(user=user)
        url = reverse(Login.name)
        data = {
            'username': email,
            'password': 'wrongpassword',
        }
        response = self.client.post(url, data, format='json')
        assert response.data['non_field_errors'][0] == 'Unable to log in with provided credentials.'
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_user_logout(self):
        """
        Ensure that the user can logout and the token is deleted
        """
        email = 'test_email@mail.com'
        password = 'test_password'
        first_name = 'test_first_name'
        last_name = 'test_last_name'
        user = self.create_user(email, password, first_name, last_name)
        token = Token.objects.create(user=user)
        url = reverse(Logout.name)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        response = self.client.post(url)
        assert response.status_code == status.HTTP_200_OK
        assert Token.objects.count() == 0
