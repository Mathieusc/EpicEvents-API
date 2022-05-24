from rest_framework import serializers

from authentication.serializers import UserSerializer
from clients.serializers import ClientSerializer
from contracts.serializers import ContractSerializer

from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    contract = ContractSerializer(read_only=True)
    support_contact = UserSerializer(read_only=True)

    class Meta:
        model = Event
        fields = [
            "id",
            "client",
            "contract",
            "status",
            "date_created",
            "date_updated",
            "attendees",
            "event_dates",
            "notes",
            "support_contact",
        ]
