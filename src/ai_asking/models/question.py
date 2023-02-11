
from django.db import models
from base_services.models import AutoTimeStampedModel, TinyIntegerField
from users.models import User


class ConversationModel(AutoTimeStampedModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "conversations"


class QuestionAnswerModel(AutoTimeStampedModel):
    id = models.AutoField(primary_key=True)
    conversation = models.ForeignKey(ConversationModel, on_delete=models.CASCADE, related_name="question_answers")
    question_content = models.CharField(max_length=1000, null=True)
    answer = models.CharField(null=True, max_length=10000)

    class Meta:
        db_table = "questions_answers"
