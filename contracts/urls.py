from django.urls import path, include

from contracts.views import ContractListCreateView, ContractRetrieveUpdateDestroyView


urlpatterns = [
    path("contracts/", ContractListCreateView.as_view(), name="contracts"),
    path(
        "contracts/<int:pk>/",
        ContractRetrieveUpdateDestroyView.as_view(),
        name="contract",
    ),
]
