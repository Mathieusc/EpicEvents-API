from django.db.models import RestrictedError

from rest_framework.response import Response
from rest_framework import status

from rest_framework.viewsets import ModelViewSet

from clients.models import Client
from clients.serializers import ClientListSerializer, ClientDetailSerializer
from clients.permissions import IsSales

from authentication.permissions import (
    ManagerAndSalesPermissions,
)

from django_filters.rest_framework import DjangoFilterBackend


class ClientViewSet(ModelViewSet):
    serializer_class = ClientListSerializer
    detail_serializer_class = ClientDetailSerializer
    permission_classes = [ManagerAndSalesPermissions]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["first_name", "email"]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()

    def get_queryset(self):
        # user Needed ?
        user = self.request.user
        clients = Client.objects.all()
        return clients
