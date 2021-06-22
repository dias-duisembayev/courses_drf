# Generated by Django 3.2.4 on 2021-06-22 10:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0004_alter_course_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='participants',
            field=models.ManyToManyField(related_name='enrolled_courses', to=settings.AUTH_USER_MODEL),
        ),
    ]
