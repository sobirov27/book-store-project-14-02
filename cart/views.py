from rest_framework.generics import ListCreateAPIView
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer


class CartListCreateApiView(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemListCreateApiView(ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    