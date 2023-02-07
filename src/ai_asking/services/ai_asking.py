import contextlib

from django.conf import settings

import openai

openai.api_key = settings.OPENAI_API_KEY


class AIAskingService:

    @classmethod
    def get_answer_from_question(cls, question: str):
        #  refer: https://platform.openai.com/docs/api-reference/completions/create
        with contextlib.suppress(Exception):
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=question,
                temperature=0.6,
            )
            answer = response.choices[0].text
        return answer