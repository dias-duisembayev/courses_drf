from rest_framework import serializers

from users .models import CustomUser
from .models import Course


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    """
    This serializer is used for Course model.
    """
    instructor = serializers.SlugRelatedField(slug_field='email', read_only=True)
    participants = serializers.SlugRelatedField(slug_field='email', many=True, read_only=True)

    def create(self, validated_data):
        """
        Creates Course object.
        """
        course = Course.objects.create(**validated_data)
        course.instructor = self.context['request'].user
        course.save()
        return course

    class Meta:
        model = Course
        fields = (
            'url',
            'name',
            'abbr',
            'description',
            'capacity',
            'year',
            'instructor',
            'participants',
        )

