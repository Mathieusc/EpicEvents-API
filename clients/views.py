from rest_framework.viewsets import ModelViewSet

from clients.models import Client
from clients.serializers import ClientListSerializer, ClientDetailSerializer


class ClientViewSet(ModelViewSet):
    serializer_class = ClientListSerializer
    detail_serializer_class = ClientDetailSerializer
    queryset = Client.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()
