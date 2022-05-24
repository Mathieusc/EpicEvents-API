from rest_framework.serializers import ModelSerializer

from authentication.serializers import UserSerializer
from clients.serializers import ClientSerializer

from contracts.models import Contract


class ContractSerializer(ModelSerializer):
    client = ClientSerializer(read_only=True)
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
