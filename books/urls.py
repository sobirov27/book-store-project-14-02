from django.urls import path
from .import views


urlpatterns = [
    path('book/', views.BookListCreateApiView.as_view()),
]