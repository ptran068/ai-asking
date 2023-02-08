import contextlib

from django.conf import settings

import openai

from ai_asking.models import QuestionModel, SubQuestionAnswerModel
from users.constants.constants import AccountType

openai.api_key = settings.OPENAI_API_KEY


class AIAskingService:

    @classmethod
    def has_asking_access(cls, user):
        has_access = True
        if user.account_type == AccountType.FREE and user.used_tokens > settings.MAX_TOKEN_NORMAL_ACCOUNT_PER_DAY:
            has_access = False
        if user.account_type == AccountType.PREMIUM and user.used_tokens > settings.MAX_TOKEN_PREMIUM_ACCOUNT_PER_DAY:
            has_access = False
        return has_access

    @classmethod
    def get_answer_from_question(cls, question: str, max_token: int, is_first_question: bool, question_id: int, user=None):
        #  refer: https://platform.openai.com/docs/api-reference/completions/create
        answer = ""
        with contextlib.suppress(Exception):
            response = cls.call_gpt_api(question, max_token)
            if response:
                answer = response.choices[0].text
                if user:
                    user.used_tokens += response.usage.get('total_tokens')
                    cls.save_question_answer(
                        is_first_question=is_first_question,
                        question=question,
                        answer=answer,
                        max_token=max_token,
                        question_id=question_id,
                        user=user
                    )
                    user.save()
        return answer

    @classmethod
    def call_gpt_api(cls, question: str, max_token: int):
        response = None
        with contextlib.suppress(Exception):
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=question,
                temperature=0.9,
                max_tokens=max_token
            )
        return response

    @classmethod
    def save_question_answer(cls, is_first_question: bool, question: str, answer: str, max_token: int, user, question_id=None):
        if is_first_question and not question_id:
            prompt = f"What is the title of this conversation about the following question:\n{question}"
            title_response = cls.call_gpt_api(prompt, max_token)
            title = title_response.choices[0].text
            new_question = QuestionModel(title=title, user_id=user.id)
            new_question.save()
            sub_ques = SubQuestionAnswerModel(question=new_question, question_content=question, answer=answer)
            sub_ques.save()
        else:
            sub_ques = SubQuestionAnswerModel(question_id=question_id, question_content=question, answer=answer)
            sub_ques.save()


