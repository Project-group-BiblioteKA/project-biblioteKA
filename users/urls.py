from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [path("loand/<int:user_id>", views.LoanView.as_view())]
