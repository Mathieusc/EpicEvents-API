from rest_framework.viewsets import ModelViewSet

from events.models import Event
from events.serializers import EventListSerializer, EventDetailSerializer

from rest_framework.permissions import IsAuthenticated
from authentication.permissions import (
    UserPermissions,
    SalesPermissions,
    SupportPermissions,
)

from django_filters.rest_framework import DjangoFilterBackend


class EventViewSet(ModelViewSet):
    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailSerializer
    permission_classes = [IsAuthenticated, SupportPermissions]
    filter_backends = [DjangoFilterBackend]
    filterset_fileds = ["client__first_name", "client__email", "event_dates"]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()

    def get_queryset(self):
        events = Event.objects.all().select_related("client")
        return events
