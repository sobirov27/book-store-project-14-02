from rest_framework.generics import ListCreateAPIView
from .models import Order
from .serializers import OrderSerializer


class OrderListCreateApiView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer