from rest_framework import viewsets


class GenericViewMixin(viewsets.ViewSet):
    service_class = None
    lookup_field = "pk"
    lookup_url_kwarg = None

