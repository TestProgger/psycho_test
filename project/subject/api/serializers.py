from rest_framework import serializers
from subject import models


class CreateSubjectSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    middle_name = serializers.CharField(allow_blank=True, allow_null=True)
    group_id = serializers.UUIDField()
    secret = serializers.CharField(required=False, allow_null=True)


class ListGroupsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubjectGroup
        fields = ('id', 'name')