# Generated by Django 3.2.4 on 2021-06-22 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_course_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='capacity',
            field=models.IntegerField(default=0),
        ),
    ]