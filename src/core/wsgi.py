"""
WSGI config for aicore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""
import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.views import debug

application = get_wsgi_application()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.development")

if settings.DEBUG:
    try:
        import warnings

        import six
        from werkzeug.debug import DebuggedApplication

        if not settings.RUNTIME_WARNING:
            warnings.filterwarnings("ignore", category=RuntimeWarning)

        def null_technical_500_response(request, exc_type, exc_value, tb):
            raise exc_value.with_traceback(tb)

        debug.technical_500_response = null_technical_500_response
        application = DebuggedApplication(application, evalex=True)
    except ImportError:
        pass
