from ai_asking.models import ConversationModel


class QuestionAnswerService:
    @classmethod
    def get_question_answers_by_user_id(cls, user_id):
        questions = ConversationModel.objects.filter(user_id=user_id)
        return questions