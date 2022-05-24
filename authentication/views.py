from rest_framework.generics import ListAPIView, RetrieveAPIView

from authentication.models import User
from authentication.serializers import UserSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
