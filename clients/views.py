from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from clients.models import Client
from clients.serializers import ClientSerializer


class ClientListCreateView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)


class ClientRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    # Add permissions
