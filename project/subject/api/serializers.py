from rest_framework import serializers


class CreateSubjectSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    middle_name = serializers.CharField(allow_blank=True, allow_null=True)
    group_id = serializers.UUIDField()