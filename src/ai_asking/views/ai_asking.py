from django.contrib.auth.models import AnonymousUser
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from ai_asking.serializers.ai_asking import AskingSerializer
from ai_asking.services.ai_asking import AIAskingService
from base_services.customized.view_mixin import GenericViewMixin
from base_services.rest_api.http import HttpMethod
from base_services.throttles.user import UserAskingThrottle


class AIAskingViewSet(GenericViewMixin):
    throttle_classes = (UserAskingThrottle,)

    @action(detail=False, methods=[HttpMethod.POST], permission_classes=())
    def ask_question(self, request):
        data = request.data.copy()
        serializer = AskingSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            is_first_ques = data.get('is_first_question') or False
            answer = AIAskingService.get_answer_from_question(
                data.get('question'), max_token=256, is_first_question=is_first_ques
            )
            data = dict(answer=answer)
            return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=[HttpMethod.POST])
    def user_ask_question(self, request):
        data = request.data.copy()
        serializer = AskingSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = request.user
            if user and AIAskingService.has_asking_access(user):
                is_first_ques = data.get('is_first_question') or False
                question_id = data.get('question_id')
                answer = AIAskingService.get_answer_from_question(
                    data.get('question'), max_token=2000,
                    is_first_question=is_first_ques, user=user, question_id=question_id
                )
                data = dict(answer=answer)
                return Response(data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)