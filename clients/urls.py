from django.urls import path, include

from rest_framework import routers

from clients.views import ClientViewSet

client_router = routers.SimpleRouter()
client_router.register("clients", ClientViewSet, basename="client")

urlpatterns = [path("", include(client_router.urls))]
