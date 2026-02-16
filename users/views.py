from rest_framework.generics import ListCreateAPIView
from .models import User
from .serializers import UserSerializer


class UserListCreateApiView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer