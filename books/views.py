from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import BookSerializer
from permissions import IsAllowed
from rest_framework.permissions import IsAuthenticated

class BookDeatilView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAllowed]

    serializer_class = BookSerializer
    lookup_url_kwarg = "book_id"
