from django.urls import path
from . import views

urlpatterns = [
    path("loand/<user_id>/", views.LoandView.as_view()),
]
