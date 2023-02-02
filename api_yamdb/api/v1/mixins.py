from rest_framework import mixins
from rest_framework import viewsets


class CreateListDeleteViewSet(mixins.DestroyModelMixin,
                              mixins.CreateModelMixin,
                              mixins.ListModelMixin,
                              viewsets.GenericViewSet):
    pass
