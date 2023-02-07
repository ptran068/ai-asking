from django.conf import settings
from django.conf.urls import include, url
from rest_framework import routers

from users.views import AuthViewSet

app_name = settings.USER
router = routers.SimpleRouter(trailing_slash=False)

router.register(r"auth", AuthViewSet, basename="AuthViewSet")

urlpatterns = [
    url(r"^", include(router.urls)),
]
