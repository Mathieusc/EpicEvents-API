from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from contracts.models import Contract
from contracts.serializers import ContractSerializer


class ContractListCreateView(ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    def perform_create(self, serializer):
        pass


class ContractRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    # Add permissions
