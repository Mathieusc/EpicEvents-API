from rest_framework.serializers import ModelSerializer

from authentication.serializers import UserSerializer

from clients.models import Client


class ClientSerializer(ModelSerializer):
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
