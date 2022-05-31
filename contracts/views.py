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

    def create(self, request, *args, **kwargs):
        """
        POST method for sales member linked to a client.
        """
        contract_data = request.data
        client = Client.objects.filter(id=contract_data["client"])
        client = client.get()
        new_contract = Contract.objects.create(
            client=client, amount=contract_data["amount"]
        )
        new_contract.save()
        serializer = ContractDetailSerializer(new_contract)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
        PUT method for sales (role 3) and management (role 1) members.
        """
        user = request.user
        data = request.data
        contract_to_update = Contract.objects.filter(
            pk=kwargs["pk"], client=data["client"]
        )
        contract = contract_to_update.get()

        if user.role == 3 or user.role == 1:
            contract.client = data["client"]
            contract.amount = data["amount"]
            contract.save()
            serializer = ContractDetailSerializer(contract)
            return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        DELETE method only for the sales member responsible of the contract.
        If an event is linked to the contract it cannot be deleted.
        """
        user = request.user
        contract_to_delete = Contract.objects.filter(pk=kwargs["pk"])
        contract = contract_to_delete.get()

        if contract.sales_contact != user:
            return Response(
                {
                    "Message:"
                    f"Only members responsible of this contract can delete it."
                },
                status=status.HTTP_403_FORBIDDEN,
            )
        try:
            contract.delete()
            return Response(
                {"Message": f"The contract (id: {kwargs['pk']}) has been deleted."},
                status=status.HTTP_204_NO_CONTENT,
            )
        except RestrictedError:
            return Response(
                {"Message": "Events are linked to this contract."},
                status=status.HTTP_400_BAD_REQUEST,
            )
