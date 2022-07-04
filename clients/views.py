from rest_framework.viewsets import ModelViewSet

from clients.models import Client
from clients.serializers import ClientListSerializer, ClientDetailSerializer

from rest_framework.permissions import IsAuthenticated
from authentication.permissions import SalesPermissions

from django_filters.rest_framework import DjangoFilterBackend


class ClientViewSet(ModelViewSet):
    serializer_class = ClientListSerializer
    detail_serializer_class = ClientDetailSerializer
    permission_classes = [IsAuthenticated, SalesPermissions]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["first_name", "email"]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()

    def get_queryset(self):
        clients = Client.objects.all()
        return clients
