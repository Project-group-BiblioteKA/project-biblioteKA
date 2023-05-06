from django.urls import path
from . import views

urlpatterns = [
    path("loand/<user_id>/", views.LoandView.as_view()),
    path("loand/return/<user_id>/", views.CheckoutBook.as_view()),
]
