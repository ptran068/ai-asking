from core.settings import env

# Application definition
USER = "users"
AI_ASKING = "ai_asking"

DJANGO_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "django.contrib.messages",
    "django.contrib.sessions",
    "storages",
    # "django_q",
    "django_celery_beat",
)
THIRD_PARTY_APPS = (
    "rest_framework",
)
IMPORT_EXPORT_USE_TRANSACTIONS = False

LOCAL_APPS = (
    USER,
    AI_ASKING,
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
