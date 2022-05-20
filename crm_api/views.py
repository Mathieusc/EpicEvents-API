# from rest_framework.viewsets import ModelViewSet

# from .models import Client, Contract, Event
# from .serializers import (
#     ClientDetailSerializer,
#     ClientListSerializer,
#     ContractDetailSerializer,
#     ContractListSerializer,
#     EventDetailSerializer,
#     EventListSerializer,
# )


# class ClientViewSet(ModelViewSet):
#     serializer_class = ClientListSerializer
#     detail_serializer_class = ClientDetailSerializer
#     queryset = Client.objects.all()

#     def get_serializer_class(self):
#         if self.action == "retrieve":
#             return self.detail_serializer_class
#         return super().get_serializer_class()


# class ContractViewSet(ModelViewSet):
#     serializer_class = ContractListSerializer
#     detail_serializer_class = ContractDetailSerializer
#     queryset = Contract.objects.all()

#     def get_serializer_class(self):
#         if self.action == "retrieve":
#             return self.detail_serializer_class
#         return super().get_serializer_class()


# class EventViewSet(ModelViewSet):
#     serializer_class = EventListSerializer
#     detail_serializer_class = EventDetailSerializer
#     queryset = Event.objects.all()

#     def get_serializer_class(self):
#         if self.action == "retrieve":
#             return self.detail_serializer_class
#         return super().get_serializer_class()
