from rest_framework.serializers import ModelSerializer

from authentication.serializers import UserSerializer

from clients.models import Client


class ClientListSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "first_name", "email", "sales_contact"]


class ClientDetailSerializer(ModelSerializer):
    sales_contact = UserSerializer(read_only=True)

    class Meta:
        model = Client
        fields = [
            "id",
            "company_name",
            "first_name",
            "last_name",
            "email",
            "phone",
            "mobile",
            "date_created",
            "date_updated",
            "sales_contact",
        ]
