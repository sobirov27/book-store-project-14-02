from rest_framework.generics import ListCreateAPIView
from .models import Author
from .serializers import AuthorSerializer


class AuthorListCreateApiView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer