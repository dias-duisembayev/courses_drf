from django.db import models

from users.models import CustomUser


class Course(models.Model):
    YEAR_CHOICES = (
        (1, '1st year'),
        (2, '2nd year'),
        (3, '3rd year'),
        (4, '4th year'),
    )
    name = models.CharField(max_length=50, unique=True)
    abbr = models.CharField(max_length=7, unique=True)
    description = models.TextField(max_length=500)
    instructor = models.ForeignKey(CustomUser, related_name='teaching_courses', on_delete=models.SET_NULL, null=True)
    participants = models.ManyToManyField(CustomUser, related_name='enrolled_courses')
    capacity = models.IntegerField(default=0)
    year = models.IntegerField(choices=YEAR_CHOICES)

    def __str__(self):
        return f'{self.abbr}: {self.name}'
