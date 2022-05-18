from django.urls import path, include

from rest_framework import routers

from crm_api.views import ClientViewSet

client_router = routers.SimpleRouter()
client_router.register("clients", ClientViewSet, basename="client")

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("", include(client_router.urls)),
]
