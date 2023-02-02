from rest_framework import mixins, viewsets


class CreateListDeleteViewSet(mixins.DestroyModelMixin,
                              mixins.CreateModelMixin,
                              mixins.ListModelMixin,
                              viewsets.GenericViewSet):
    pass
