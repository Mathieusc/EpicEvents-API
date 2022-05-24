from rest_framework.serializers import ModelSerializer

from authentication.serializers import UserSerializer
from clients.serializers import ClientListSerializer

from contracts.models import Contract


class ContractListSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ["id", "client", "amount", "date_created"]


class ContractDetailSerializer(ModelSerializer):
    client = ClientListSerializer(read_only=True)
    sales_contact = UserSerializer(read_only=True)

    class Meta:
        model = Contract
        fields = [
            "id",
            "client",
            "sales_contact",
            "date_created",
            "date_updated",
            "amount",
            "payment_due",
            "is_finished",
            "is_paid",
        ]
