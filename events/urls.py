from django.urls import path, include

from events.views import EventListCreateView, EventRetrieveUpdateDestroyView

urlpatterns = [
    path("events/", EventListCreateView.as_view(), name="events"),
    path("events/<int:pk>/", EventRetrieveUpdateDestroyView.as_view(), name="event"),
]
