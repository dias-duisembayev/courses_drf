# Generated by Django 3.2.4 on 2021-06-22 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='capacity',
            field=models.IntegerField(default=1),
        ),
    ]