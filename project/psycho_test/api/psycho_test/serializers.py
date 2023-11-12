from rest_framework import serializers
from psycho_test import models


class ListPsychoTestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PsychoTest
        exclude = ('created_at', 'updated_at')


class StartPsychoTestSerializer(serializers.Serializer):
    id = serializers.UUIDField()


class EndPsychoTestSerializer(serializers.Serializer):
    id = serializers.UUIDField()