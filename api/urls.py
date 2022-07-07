from django.urls import path
from .views import BookAPIView, DetailBookAPIView, CreateBookAPIView


urlpatterns = [
    path('', BookAPIView.as_view()),
    path('<int:pk>/', DetailBookAPIView.as_view()),
    path('create/', CreateBookAPIView.as_view()),
]
