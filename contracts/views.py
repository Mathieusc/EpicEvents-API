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

    def create(self, request, *args, **kwargs):
        """
        POST method for sales member linked to a client.
        """
        contract_data = request.data
        client = Client.objects.filter(id=contract_data["client"])
        client = client.get()
        print(client)
        new_contract = Contract.objects.create(
            client=client, amount=contract_data["amount"]
        )
        new_contract.save()
        serializer = ContractDetailSerializer(new_contract)
        return Response(serializer.data)
