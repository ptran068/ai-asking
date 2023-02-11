from rest_framework import serializers

from ai_asking.models import ConversationModel, QuestionAnswerModel


class SubQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswerModel
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    question_answers = SubQuestionSerializer(many=True, required=False)

    class Meta:
        model = ConversationModel
        fields = ['title', 'id', 'question_answers']


class EditConvoSerializer(serializers.Serializer):
    title = serializers.CharField(allow_blank=False, allow_null=False, max_length=255)
