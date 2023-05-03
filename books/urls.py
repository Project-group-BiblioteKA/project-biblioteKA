from django.urls import path
from . import views

urlpatterns = [
     path('book/', views.BookCreateView.as_view()),
     path('book/<book_id>/', views.BookDetailView.as_view()),
]
