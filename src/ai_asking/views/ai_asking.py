from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from ai_asking.serializers.ai_asking import AskingSerializer
from ai_asking.services.ai_asking import AIAskingService
from base_services.customized.view_mixin import GenericViewMixin
from base_services.rest_api.http import HttpMethod


class AIAskingViewSet(GenericViewMixin):
    authentication_classes = ()
    permission_classes = ()

    @action(detail=False, methods=[HttpMethod.POST])
    def ask_question(self, request):
        data = request.data.copy()
        serializer = AskingSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            answer = AIAskingService.get_answer_from_question(data.get('question'))
            data = dict(answer=answer)
            return Response(data, status=status.HTTP_200_OK)
