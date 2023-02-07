import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

from core.settings.configs import celery_config
from store_queue_tasks.tasks.base import CeleryBaseTask

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.development')

app = Celery("store_queue_tasks", broker='redis://127.0.0.1:6379')
app.Task = CeleryBaseTask
app.config_from_object(celery_config)
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

import datetime
now = datetime.datetime.now()

app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'get_added_emails_in_current_month': {
        'task': 'store_queue_tasks.tasks.get_added_emails.get_current_mails',
        'schedule': crontab(hour=9, minute=44)
    },

}

