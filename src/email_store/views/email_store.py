from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from base_services.customized.view_mixin import GenericViewMixin
from base_services.rest_api.http import HttpMethod
from email_store.serializers.email_store import EmailStoreSerializer, ListEmailStoreSerializer
from email_store.services.email_store import EmailStoreService


class EmailStoreViewSet(GenericViewMixin):
    @action(detail=False, methods=[HttpMethod.POST])
    def save_email(self, request):
        data = request.data.copy()
        serializer = EmailStoreSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        email_stores_data = EmailStoreService.get_list_emails_store()
        email_stores = ListEmailStoreSerializer(email_stores_data.get('email_stores'), many=True).data
        data = dict(
            total_current_month_emails=email_stores_data.get('total_current_month_emails'),
            total_unsubscribed=email_stores_data.get('total_unsubscribed'),
            email_stores=email_stores
        )
        return Response(data, status=status.HTTP_200_OK)
