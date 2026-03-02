from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/user/v1/login/', TokenObtainPairView.as_view()),
    path('api/books', include('books.urls')), 
    path('api/authors', include('authors.urls')),
    path('api/orders', include('orders.urls')), 
    path('api/users', include('users.urls')),
    path('api/cart', include('cart.urls')), 
]
