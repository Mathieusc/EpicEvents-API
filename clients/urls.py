from django.urls import path, include

from clients.views import ClientListCreateView, ClientRetrieveUpdateDestroyView


urlpatterns = [
    path("clients/", ClientListCreateView.as_view(), name="clients"),
    path("clients/<int:pk>/", ClientRetrieveUpdateDestroyView.as_view(), name="client"),
]
