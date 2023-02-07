from rest_framework import serializers


class AskingSerializer(serializers.Serializer):
    question = serializers.CharField(required=True, max_length=1000) # customize format, unique error if needed

