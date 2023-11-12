from rest_framework import serializers
from psycho_test import models


class ListPsychoTestModelSerializer(serializers.ModelSerializer):
    questions_count = serializers.SerializerMethodField()

    def get_questions_count(self, obj):
        return models.PsychoTestToQuestion.objects.filter(psycho_test_id=obj).count()

    class Meta:
        model = models.PsychoTest
        exclude = ('created_at', 'updated_at', 'is_visible')


class StartPsychoTestSerializer(serializers.Serializer):
    id = serializers.UUIDField()


class EndPsychoTestSerializer(serializers.Serializer):
    id = serializers.UUIDField()