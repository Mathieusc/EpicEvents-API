from django.urls import path, include

from rest_framework import routers

from contracts.views import ContractViewSet

client_router = routers.SimpleRouter()
client_router.register("contracts", ContractViewSet, basename="contract")

urlpatterns = [path("", include(client_router.urls))]
