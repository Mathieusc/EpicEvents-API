from django.db.models import RestrictedError

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from clients.models import Client
from contracts.models import Contract
from contracts.serializers import ContractListSerializer, ContractDetailSerializer


class ContractViewSet(ModelViewSet):
    serializer_class = ContractListSerializer
    detail_serializer_class = ContractDetailSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()

    def get_queryset(self):
        user = self.request.user
        contracts = Contract.objects.all()
        return contracts
