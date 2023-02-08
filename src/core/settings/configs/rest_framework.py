REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'middlewares.authentication.AuthenticationJWT',
    ],
    "EXPIRED_FOREVER": "2000-10-10 00:00:00",
    "DEFAULT_THROTTLE_RATES": {
        "normal_user": "15/minute",
        "premium_user": "60/minute",
    },
    "OVERRIDE_THROTTLE_RATES": {"special": "10000/hour"},
}

REST_FRAMEWORK_CACHE = {
    "DEFAULT_CACHE_TIMEOUT": 86400,  # Default is 1 day
}
