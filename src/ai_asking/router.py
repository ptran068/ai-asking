
from django.conf import settings
from django.conf.urls import include, url
from rest_framework import routers

from ai_asking.views import AIAskingViewSet, QuestionAnswerViewSet

app_name = settings.AI_ASKING
router = routers.SimpleRouter(trailing_slash=False)

router.register(r"ai", AIAskingViewSet, basename="AskingViewSet")
router.register(r"question", QuestionAnswerViewSet, basename="QuestionAnswerViewSet")

urlpatterns = [
    url(r"^", include(router.urls)),
]
