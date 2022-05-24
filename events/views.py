from rest_framework.viewsets import ModelViewSet

from events.models import Event
from events.serializers import EventSerializer


class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
