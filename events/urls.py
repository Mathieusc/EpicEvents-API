from django.urls import path, include

from rest_framework import routers

from events.views import EventViewSet

client_router = routers.SimpleRouter()
client_router.register("events", EventViewSet, basename="event")

urlpatterns = [path("", include(client_router.urls))]
