from rest_framework import serializers

from users .models import CustomUser
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    """
    This serializer is used for creating a course
    """
    instructor = serializers.SlugRelatedField(queryset=CustomUser.objects, slug_field='email')
    participants = serializers.SlugRelatedField(queryset=CustomUser.objects, slug_field='email', many=True)

    def create(self, validated_data):
        """
        Creates CustomUser object.
        """
        course = Course.objects.create(**validated_data)
        course.instructor = self.context['request'].user
        course.save()
        return course

    class Meta:
        model = Course
        fields = (
            'name',
            'abbr',
            'description',
            'capacity',
            'year',
            'instructor',
            'participants',
        )
        extra_kwargs = {
            'instructor': {'read_only': True},
            'participants': {'read_only': True},
        }
