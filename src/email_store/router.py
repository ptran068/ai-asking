from email_store.views import *
from django.conf import settings
from django.conf.urls import include, url
from rest_framework import routers

app_name = settings.EMAIL_STORE
router = routers.SimpleRouter(trailing_slash=False)

router.register(r"email_store", EmailStoreViewSet, basename="EmailStoreViewSet")

urlpatterns = [
    url(r"^", include(router.urls)),
]
