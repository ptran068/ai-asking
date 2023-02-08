from ai_asking.models import SubQuestionAnswerModel, QuestionModel


class QuestionAnswerService:
    @classmethod
    def get_question_answers_by_user_id(cls, user_id):
        questions = QuestionModel.objects.filter(user_id=user_id)
        # for ques in questions:
        #     questions.sub_question_answer = SubQuestionAnswerModel.objects.filter(question_id=ques.id)

        return questions