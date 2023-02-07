from email_store.models import EmailStoreModel
from email_store.services.email_store import EmailStoreService
from store_queue_tasks.celery import app as celery_app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@celery_app.task
def get_current_mails():
    logger.info("start scheduler.........")

    email_stores = EmailStoreModel.objects.all()
    total = EmailStoreService.count_total_added_emails_current_month(email_stores)
    logger.info(f"Total added emails in this month: {total}")

