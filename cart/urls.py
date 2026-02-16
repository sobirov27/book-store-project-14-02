from django.urls import path
from .import views


urlpatterns = [
    path('cart/', views.CartListCreateApiView.as_view()),
    path('cartitem/', views.CartItemListCreateApiView.as_view()),
]