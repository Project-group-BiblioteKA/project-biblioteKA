from django.shortcuts import get_object_or_404

from books.models import Book
from books.serializers import BookNewSerializer
from .models import User
from .serializers import *
from .permissions import *
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import *
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import generics


class ListCreateUserview(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsColaborator]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_url_kwarg = "user_id"


class UserStatusView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "user_id"

    def to_representation(self, instance):
        status = "unavailable" if instance.is_blocked else "available"
        return {"status": status}

    def get(self, req, *args, **kwargs):
        instance = self.get_object()
        return Response(self.to_representation(instance), status=200)


class BookFollowersView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = FollowerBookSerializer

    model = BookFollower
    lookup_url_kwarg = "book_id"
    fields = ["books"]
    queryset = BookFollower.objects.all()

    def perform_create(self, serializer):
        book_id = self.kwargs["book_id"]
        user = get_object_or_404(User, id=self.request.user.id)
        book = get_object_or_404(Book, id=book_id)
        serializer.save(users=user, books=book)


class FollowerRetrieveView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsColaborator]
    serializer_class = BookNewSerializer
    lookup_url_kwarg = "book_id"
    queryset = Book
