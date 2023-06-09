from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/", views.ListCreateUserview.as_view()),
    path("users/register/", views.CreateUserView.as_view()),
    path("users/<user_id>/", views.UserDetailView.as_view()),
    path("users/status/<user_id>/", views.UserStatusView.as_view()),
    path("follower/<book_id>/", views.BookFollowersView.as_view()),
    path("followers/<book_id>/", views.FollowerRetrieveView.as_view()),
    path("login/", jwt_views.TokenObtainPairView.as_view()),
]
