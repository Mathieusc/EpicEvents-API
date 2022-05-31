from django.db.models import RestrictedError

from rest_framework.response import Response
from rest_framework import status

from rest_framework.viewsets import ModelViewSet

from clients.models import Client
from clients.serializers import ClientListSerializer, ClientDetailSerializer


class ClientViewSet(ModelViewSet):
    serializer_class = ClientListSerializer
    detail_serializer_class = ClientDetailSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return self.detail_serializer_class
        return super().get_serializer_class()

    def get_queryset(self):
        # user Needed ?
        user = self.request.user
        clients = Client.objects.all()
        return clients

    # def create(self, request, *args, **kwargs):
    #     """
    #     POST method for sales member.
    #     """
    #     client_data = request.data
    #     serializer = ClientDetailSerializer(data=client_data, partial=True)
    #     client_data._mutable = True
    #     client_data["sales_contact"] = request.user
    #     client_data._mutable = False
    #     if serializer.is_valid():
    #         client = serializer.create(client_data)
    #         return Response(client, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        """
        POST method for sales member.
        """
        # Get the data first
        client_data = request.data
        # Create the new client object
        new_client = Client.objects.create(
            first_name=client_data["first_name"], email=client_data["email"]
        )
        new_client.save()
        # Send the data (serialize data and send the response)
        serializer = ClientDetailSerializer(new_client)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """
        PUT method for sales (role 3) and management (role 1) members.
        """
        # Get the objects, fields -> new value
        # Save new object and return response
        user = request.user
        data = request.data
        client_to_update = Client.objects.filter(pk=kwargs["pk"])
        client = client_to_update.get()

        if user.role == 3 or user.role == 1:
            # client.company_name = data["company_name"]
            client.first_name = data["first_name"]
            # client.last_name = data["last_name"]
            client.email = data["email"]
            # client.phone = data["phone"]
            # client.mobile = data["mobile"]

            client.save()
            serializer = ClientDetailSerializer(client)
            return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        DELETE method only for the sales member responsible of the client.
        If a contract is linked to the client it cannot be deleted.
        """
        user = request.user
        client_to_delete = Client.objects.filter(pk=kwargs["pk"])
        client_to_delete = client_to_delete.get()

        if user.role == 3 and user.id != client_to_delete.sales_contact.id:
            return Response(
                {"Message:" f"Only members responsible of this client can delete it."},
                status=status.HTTP_403_FORBIDDEN,
            )
        try:
            client_to_delete.delete()
            return Response(
                {"Message": f"The client (id: {kwargs['pk']}) has been deleted."},
                status=status.HTTP_204_NO_CONTENT,
            )
        except RestrictedError:
            return Response(
                {"Message": "Contracts are linked to this client."},
                status=status.HTTP_400_BAD_REQUEST,
            )
