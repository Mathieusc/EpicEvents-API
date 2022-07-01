from rest_framework.viewsets import ModelViewSet

from authentication.models import User
from authentication.serializers import UserSerializer, RegisterUserSerializer
from authentication.permissions import ManagerPermissions


class UserViewSet(ModelViewSet):
    serializer_class = RegisterUserSerializer
    permission_classes = [ManagerPermissions]
    queryset = User.objects.all()
    http_method_names = ["post"]
