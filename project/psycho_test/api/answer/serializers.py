from rest_framework import serializers


class SetAnswerSerializer(serializers.Serializer):
    question_id = serializers.UUIDField()
    answer_id = serializers.UUIDField(allow_null=True, required=False)
    answer_ids = serializers.ListSerializer(
        child=serializers.UUIDField(), allow_null=True, allow_empty=True, required=False
    )