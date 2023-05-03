from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import BookSerializer
from .permissions import IsAllowed
from .models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
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

