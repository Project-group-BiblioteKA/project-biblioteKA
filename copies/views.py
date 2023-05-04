from django.shortcuts import render
from rest_framework import generics
from copies.models import Copy, LoandBook
from copies.serializers import LoandSerializer
from django.shortcuts import get_object_or_404
from users.models import User
from users.permissions import IsColaborator, IsStudentAble
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
class LoandView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = LoandSerializer
    permission_classes = [IsAuthenticated, IsStudentAble]
    lookup_url_kwarg = "user_id"

    def get_queryset(self):
        pk = self.kwargs["user_id"]
        user = get_object_or_404(User, id=pk)
        return LoandBook.objects.filter(users_id=user)

    def perform_create(self, serializer):
        pk = self.kwargs["user_id"]
        user = get_object_or_404(User, id=pk)
        copy_id = self.request.data["copy_id"]
        copy = get_object_or_404(Copy, id=copy_id)
        copy.is_avaliable = False
        copy.save()

        serializer.save(users=user, copy=copy)


class LoandDetailView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = LoandSerializer
    lookup_url_kwarg = "user_id"
    permission_classes = [IsAuthenticated, IsColaborator]
    queryset = LoandBook.objects.all()
