from rest_framework import serializers


class ListQuestionSerializer(serializers.Serializer):
    id = serializers.UUIDField()