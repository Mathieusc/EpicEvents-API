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


class ContractListSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ["id", "client", "amount", "date_created"]


class ContractDetailSerializer(ModelSerializer):
    client_email = serializers.ReadOnlyField(source="client.email")

    class Meta:
        model = Contract
        fields = [
            "id",
            "client",
            "client_email",
            "date_created",
            "date_updated",
            "status",
            "amount",
            "payment_due",
        ]


class EventListSerializer(ModelSerializer):
    client_email = serializers.ReadOnlyField(source="client.email")

    class Meta:
        model = Event
        fields = ["id", "contract", "client_email", "event_dates"]


class EventDetailSerializer(ModelSerializer):
    client_company_name = serializers.ReadOnlyField(source="client.company_name")

    class Meta:
        model = Event
        fields = [
            "id",
            "client_company_name",
            "status",
            "date_created",
            "date_updated",
            "attendees",
            "event_dates",
            "notes",
        ]
