from rest_framework import viewsets, mixins


class ListCreateViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pass
