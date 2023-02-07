from email_store.constants.constants import EmailStatus
from email_store.models import EmailStoreModel
from datetime import datetime
from django.db.models.query import QuerySet


class EmailStoreService:
    @classmethod
    def get_list_emails_store(cls):
        email_stores = EmailStoreModel.objects.order_by('-created_at')
        total_current_month_emails = cls.count_total_added_emails_current_month(email_stores)
        total_unsubscribed = cls._count_total_unsubscribed(email_stores)
        data = dict(
            email_stores=email_stores,
            total_current_month_emails=total_current_month_emails,
            total_unsubscribed=total_unsubscribed
        )
        return data

    @classmethod
    def count_total_added_emails_current_month(cls, email_stores: [QuerySet]):
        current_month = datetime.now().month
        total_current_month_emails = email_stores.filter(created_at__month=current_month).count()
        return total_current_month_emails

    @classmethod
    def _count_total_unsubscribed(cls, email_stores: [QuerySet]):
        return email_stores.filter(status=EmailStatus.UNSUBSCRIBED).count()