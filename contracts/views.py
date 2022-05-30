from rest_framework.viewsets import ModelViewSet

from contracts.models import Contract
from contracts.serializers import ContractListSerializer, ContractDetailSerializer


class ContractViewSet(ModelViewSet):
    serializer_class = ContractListSerializer
    detail_serializer_class = ContractDetailSerializer
    queryset = Contract.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()
