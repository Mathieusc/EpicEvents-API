from rest_framework.viewsets import ModelViewSet

from events.models import Event
from events.serializers import EventListSerializer, EventDetailSerializer

from authentication.permissions import SupportPermissions, ManagerAndSalesPermissions

from django_filters.rest_framework import DjangoFilterBackend


class EventViewSet(ModelViewSet):
    serializer_class = EventListSerializer
    detail_serializer_class = EventDetailSerializer
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_fileds = ["client__first_name", "client__email", "event_dates"]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()

    def get_queryset(self):
        user = self.request.user
        events = Event.objects.all()
        return events
