from os.path import dirname, join
from core.settings import env
from core.settings import BASE_DIR
from core.settings import __version__

STATICFILES_DIRS = [join(BASE_DIR, "")]
MEDIA_ROOT = join(BASE_DIR, "media")
ALLOWED_HOSTS = env.list(
    "DJANGO_ALLOWED_HOSTS", default=["localhost", "127.0.0.1"]
)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
# Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env("SECRET_KEY")
CSRF_COOKIE_SECURE = True
API_HOST = env("API_HOST")
API_PORT = env.int("API_PORT")
ROOT_URLCONF = "core.urls"
WSGI_APPLICATION = "core.wsgi.application"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = False
USE_TZ = True
# Log everything to the logs directory at the top
LOGFILE_ROOT = env("LOGFILE_ROOT", default=join(dirname(BASE_DIR), "logs"))
# Doc file
VERSION_NUMBER = env("VERSION_NUMBER", default=__version__)
DATA_UPLOAD_MAX_NUMBER_FIELDS = env.int("DATA_UPLOAD_MAX_NUMBER_FIELDS", default=4000)
STATIC_URL = "/static/"

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]
AUTH_USER_MODEL = 'users.User'

JWT_AUTH = {
    'JWT_PUBLIC_KEY': open(dirname(BASE_DIR) + '/pub_key.pem', 'rb').read(),
    'JWT_PRIVATE_KEY': open(dirname(BASE_DIR) + '/privkey.pem', 'rb').read(),
    'JWT_ALGORITHM': 'RS256',
}