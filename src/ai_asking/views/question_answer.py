from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from ai_asking.models import ConversationModel
from ai_asking.serializers.question import QuestionSerializer, QuestionAnswerModel, EditConvoSerializer
from ai_asking.services.question_answer import QuestionAnswerService
from base_services.customized.view_mixin import GenericViewMixin
from base_services.rest_api.http import HttpMethod


class QuestionAnswerViewSet(GenericViewMixin):

    @action(detail=False, methods=[HttpMethod.GET])
    def list_questions(self, request, **kwargs):
        questions = QuestionAnswerService.get_question_answers_by_user_id(request.user.id)
        questions = QuestionSerializer(questions, many=True).data
        data = dict(data=questions)
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=True, methods=[HttpMethod.PUT])
    def edit_conversation(self, request, pk=None, *args, **kwargs):
        data = request.data.copy()
        serializer = EditConvoSerializer(data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            ConversationModel.objects.filter(id=pk).update(title=data.get('title'))
            return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=[HttpMethod.DELETE])
    def delete_question(self, request, pk=None, *args, **kwargs):
        ConversationModel.objects.filter(id=pk).delete()
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=[HttpMethod.DELETE])
    def delete_multi_question(self, request, *args, **kwargs):
        ConversationModel.objects.filter(user_id=request.user.id).delete()
        return Response(status=status.HTTP_200_OK)