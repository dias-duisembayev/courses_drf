# Generated by Django 3.2.4 on 2021-06-22 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='capacity',
            field=models.IntegerField(default=20),
        ),
    ]
