from django.urls import path
from .import views


urlpatterns = [
    path('user/', views.UserListCreateApiView.as_view()),
    
]