from rest_framework.viewsets import ModelViewSet

from authentication.models import User
from authentication.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
