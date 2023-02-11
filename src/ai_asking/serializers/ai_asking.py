from rest_framework import serializers


class AskingSerializer(serializers.Serializer):
    question = serializers.CharField(required=True, max_length=1000)
    is_first_question = serializers.BooleanField(required=False, allow_null=True)
    conversation_id = serializers.IntegerField(required=False, allow_null=True)

