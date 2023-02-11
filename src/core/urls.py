from django.conf.urls import include, url
from django.views.generic import RedirectView


urlpatterns = [
    url(r"^docs$", RedirectView.as_view(url="docs/")),
    url(r"^api/v1/", include("users.router", namespace="v1")),
    url(r"^api/v1/", include("ai_asking.router", namespace="v1")),
]

urlpatterns += (url(r"^favicon\.ico$", RedirectView.as_view(url="/docs/img/favicon.ico")),)

