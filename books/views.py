from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import BookSerializer
from .permissions import IsAllowed
from .models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BookCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAllowed]

    serializer_class = BookSerializer


class BookRetrieveView(generics.ListAPIView):
    
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAllowed]

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = "book_id"

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
