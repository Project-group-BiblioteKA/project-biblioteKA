from django.urls import path
from . import views


urlpatterns = [
     path('books/', views.BookDetailView.as_view()),
]
