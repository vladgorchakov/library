from django.urls import path
from .views import BookAPIView, DetailBookAPIView, CreateBookAPIView,\
    CreateAuthorAPIView, DetailAuthorAPIView, AuthorListAPIView


urlpatterns = [
    path('books/', BookAPIView.as_view()),
    path('books/<int:pk>/', DetailBookAPIView.as_view()),
    path('books/add/', CreateBookAPIView.as_view()),
    path('authors/', AuthorListAPIView.as_view()),
    path('authors/add/', CreateAuthorAPIView.as_view(),),
    path('authors/<int:pk>', DetailAuthorAPIView.as_view()),
]
