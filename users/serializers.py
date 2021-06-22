from rest_framework import serializers

from .models import CustomUser


class StudentRegistrationSerializer(serializers.ModelSerializer):
    """
    This serializer is used for registration of Students (CustomUser
    with is_teacher field set to False).
    """
    def create(self, validated_data):
        """
        Creates CustomUser object.
        """
        user = CustomUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'password',
            'first_name',
            'last_name',
            'year',
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }


class TeacherRegistrationSerializer(serializers.ModelSerializer):
    """
    This serializer is used for registration of Teachers (CustomUser
    with is_teacher field set to True).
    """
    def create(self, validated_data):
        """
        Creates CustomUser object with is_teacher filed set to True.
        """
        user = CustomUser.objects.create(is_teacher=True, **validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'password',
            'first_name',
            'last_name',
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }


class CustomUserLoginSerializer(serializers.ModelSerializer):
    """
    This serializer is used for login of CustomUser.
    """
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'password',
        )
