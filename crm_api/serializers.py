from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Client, Contract, Event


class ClientListSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "first_name", "email"]


class ClientDetailSerializer(ModelSerializer):
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
            "sales",
        ]
