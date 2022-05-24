from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from events.models import Event
from events.serializers import EventSerializer


class EventListCreateView(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # Add permissions

    def perform_create(self, serializer):
        pass


class EventRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # Add permissions
