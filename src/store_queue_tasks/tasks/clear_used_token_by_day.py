from email_store.models import EmailStoreModel
from email_store.services.email_store import EmailStoreService
from store_queue_tasks.celery import app as celery_app
from celery.utils.log import get_task_logger

from users.models import User

logger = get_task_logger(__name__)


@celery_app.task
def clear_used_tokens():
    logger.info("start clear used tokens.........")

    User.objects.update(used_tokens=0)

    logger.info(f"...............Done.................")

