from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model extending AbstractBaseUser model
    Username fields was changed to email
    Additional boolean field is_teacher added to distinguish users between
    students and teachers.
    """
    YEAR_CHOICES = (
        (1, '1st year'),
        (2, '2nd year'),
        (3, '3rd year'),
        (4, '4th year'),
    )
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    start_date = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    year = models.IntegerField(default=1, choices=YEAR_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'is_teacher']

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)
