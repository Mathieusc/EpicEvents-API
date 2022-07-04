from rest_framework import serializers

from authentication.serializers import UserSerializer

from events.models import Event


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "client",
            "contract",
            "event_dates",
            "status",
            "attendees",
            "support_contact",
        ]


class EventDetailSerializer(serializers.ModelSerializer):
    support_contact = UserSerializer(read_only=True)

    class Meta:
        model = Event
        fields = [
            "id",
            "client",
            "contract",
            "status",
            "event_dates",
            "date_created",
            "date_updated",
            "attendees",
            "notes",
            "support_contact",
        ]
