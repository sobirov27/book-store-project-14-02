from django.urls import path
from .import views


urlpatterns = [
    path('author/', views.AuthorListCreateApiView.as_view()),
]