from .base import *  # NOQA
from os.path import sys

from logging.config import dictConfig

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True

# Turn off debug while imported by Celery with a workaround
# See http://stackoverflow.com/a/4806384
if "celery" in sys.argv[0]:
    DEBUG = False

STATIC_URL = join(BASE_DIR, "static/")
# Show thumbnail generation errors
THUMBNAIL_DEBUG = True

# Reset logging
# (see http://www.caktusgroup.com/blog/2015/01/27/Django-Logging-Configuration-logging_config-default-settings-logger/)

DEVELOPMENT_LOGGING_CONFIG = {
    "DJANGO": {
        "FORMATTER": env("DJANGO_LOG_FORMATTER", default="verbose"),
        "LEVEL": env("DJANGO_LOG_LEVEL", default="DEBUG"),
    },
    "PROJECT": {
        "FORMATTER": env("PROJECT_LOG_FORMATTER", default="verbose"),
        "LEVEL": env("PROJECT_LOG_LEVEL", default="DEBUG"),
    },
    "CONSOLE": {
        "FORMATTER": env("CONSOLE_LOG_FORMATTER", default="simple"),
        "LEVEL": env("CONSOLE_LOG_LEVEL", default="DEBUG"),
    },
    # "QUEUE": {
    #     "FORMATTER": env("QUEUE_LOG_FORMATTER", default="simple"),
    #     "LEVEL": env("QUEUE_LOG_LEVEL", default="INFO"),
    # },
    "QUERY": {"LEVEL": env("QUERY_LOG_LEVEL", default="INFO")},
}
LOGGING_CONFIG = None
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s] %(message)s",
            "datefmt": "%d/%b/%Y %H:%M:%S",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
        "s3_json": {"format": ""},  # Lets each Logclass format the json data
    },
    "handlers": {
        "django_log_file": {
            "level": DEVELOPMENT_LOGGING_CONFIG.get("DJANGO").get("LEVEL"),
            "class": "logging.FileHandler",
            "filename": join(LOGFILE_ROOT, "django.log"),
            "formatter": DEVELOPMENT_LOGGING_CONFIG.get("DJANGO").get("FORMATTER"),
        },
        "proj_log_file": {
            "level": DEVELOPMENT_LOGGING_CONFIG.get("PROJECT").get("LEVEL"),
            "class": "logging.FileHandler",
            "filename": join(LOGFILE_ROOT, "core.log"),
            "formatter": DEVELOPMENT_LOGGING_CONFIG.get("PROJECT").get("FORMATTER"),
        },
        "console": {
            "level": DEVELOPMENT_LOGGING_CONFIG.get("CONSOLE").get("LEVEL"),
            "class": "logging.StreamHandler",
            "formatter": DEVELOPMENT_LOGGING_CONFIG.get("CONSOLE").get("FORMATTER"),
        },
        "query": {
            "level": DEVELOPMENT_LOGGING_CONFIG.get("QUERY").get("LEVEL"),
            "class": "logging.FileHandler",
            "filename": join(LOGFILE_ROOT, "queries.log"),
            "formatter": DEVELOPMENT_LOGGING_CONFIG.get("QUERY").get("FORMATTER"),
        },
    },
    "loggers": {
        "console": {
            "handlers": ["console"],
            "propagate": True,
            "level": "DEBUG",
        },
        "django.server": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
        "project": {
            "handlers": ["proj_log_file"],
            "level": DEVELOPMENT_LOGGING_CONFIG.get("PROJECT").get("LEVEL"),
        },
        "django.db.backends": {
            "handlers": ["query"],
            "level": DEVELOPMENT_LOGGING_CONFIG.get("QUERY").get("LEVEL"),
            "propagate": False,
        },
    },
}

dictConfig(LOGGING)
#
# Store file to EMAIL_FILE_PATH/receiver.html instead of send to receiver email
#
EMAIL_BACKEND = "aicore.mail.FileBackend"
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_FILE_PATH = "sent_emails"

# Cache the templates in memory for speed-up
loaders = [
    (
        "django.template.loaders.cached.Loader",
        [
            "django.template.loaders.filesystem.Loader",
            "django.template.loaders.app_directories.Loader",
        ],
    ),
]

TEMPLATES[0]["OPTIONS"].update({"loaders": loaders})

OPENAI_API_KEY = env('OPENAI_API_KEY')
