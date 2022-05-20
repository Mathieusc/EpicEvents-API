from django.urls import path, include

from rest_framework import routers

# from crm_api.views import ClientViewSet, ContractViewSet, EventViewSet

# client_router = routers.SimpleRouter()
# client_router.register("clients", ClientViewSet, basename="client")

# contract_router = routers.SimpleRouter()
# contract_router.register("contracts", ContractViewSet, basename="contract")

# event_router = routers.SimpleRouter()
# event_router.register("events", EventViewSet, basename="event")

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    # path("", include(client_router.urls)),
    # path("", include(contract_router.urls)),
    # path("", include(event_router.urls)),
]
