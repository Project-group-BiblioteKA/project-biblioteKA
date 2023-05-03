from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView
)


class ListCreateUserview(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer

<<<<<<< HEAD
    lookup_url_kwarg = "user_id"
=======
    lookup_url_kwarg = 'user_id'

class UserStatusView(RetrieveAPIView):
    queryset = User.objects.all()
    lookup_field = "id"
    lookup_url_kwarg = "user_id"

    def to_representation(self,instance):
        status = "unavailable" if instance.is_blocked else "available"
        return {"status": status}
    
    
    def get(self, req, *args, **kwargs):
        instance = self.get_object()
        return Response(self.to_representation(instance), status=200)
>>>>>>> 10224affc175a23c1aac89f2c0ada3bb7dfdfdda
