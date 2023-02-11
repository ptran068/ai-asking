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
    # Executes every 00:00
    'clear_used_token_by_day': {
        'task': 'store_queue_tasks.tasks.clear_used_token_by_day.clear_used_tokens',
        'schedule': crontab(hour=0, minute=0)
    },

}

