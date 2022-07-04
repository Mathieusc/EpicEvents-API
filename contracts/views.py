from rest_framework.viewsets import ModelViewSet

from contracts.models import Contract
from contracts.serializers import ContractListSerializer, ContractDetailSerializer

from rest_framework.permissions import IsAuthenticated
from authentication.permissions import SalesPermissions

from django_filters.rest_framework import DjangoFilterBackend


class ContractViewSet(ModelViewSet):
    serializer_class = ContractListSerializer
    detail_serializer_class = ContractDetailSerializer
    permission_classes = [IsAuthenticated, SalesPermissions]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["client__first_name", "client__email", "date_created", "amount"]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()

    def get_queryset(self):
        contracts = Contract.objects.all().select_related("client")
        return contracts
