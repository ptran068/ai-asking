from core.settings import env

CELERY_IMPORTS = [
    # task modules
    "store_queue_tasks.tasks.get_added_emails",
]

CELERY_BROKER_URL = f'redis://{env("REDIS_HOST")}:{env("REDIS_PORT")}'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERY_TASK_TRACK_STARTED = True
# CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_ENABLE_UTC = True
# CELERY_RESULT_BACKEND = 'django-db'

#CELERY BEAT SETTINGS

CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
