"""
Django settings for aicore project.
For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
LOG_WEBAPP = "project"
LOG_QUEUE = "queue"

from core.settings.configs.templates import *  # noqa
from core.settings.configs.databases import *  # noqa
from core.settings.configs.middlewares import *  # noqa
from core.settings.configs.rest_framework import *  # noqa
from core.settings.configs.installed_apps import *  # noqa
from core.settings.configs.throttle import *  # noqa
from core.settings.configs.general import *  # noqa
from core.settings.configs.celery_config import *  # noqa
