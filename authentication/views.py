from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from authentication.models import User
from authentication.serializers import RegisterUserSerializer
from authentication.permissions import ManagerPermissions


class UserViewSet(ModelViewSet):
    serializer_class = RegisterUserSerializer
    permission_classes = [IsAuthenticated, ManagerPermissions]
    queryset = User.objects.all()
    http_method_names = ["post"]
