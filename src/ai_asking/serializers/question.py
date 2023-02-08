from rest_framework import serializers

from ai_asking.models import QuestionModel, SubQuestionAnswerModel


class SubQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubQuestionAnswerModel
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    sub_question_answer = SubQuestionSerializer(many=True, required=False)

    class Meta:
        model = QuestionModel
        fields = ['title', 'id', 'sub_question_answer']


class EditQuestionSerializer(serializers.Serializer):
    title = serializers.CharField(allow_blank=False, allow_null=False, max_length=255)
