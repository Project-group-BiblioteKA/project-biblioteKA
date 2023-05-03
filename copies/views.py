from django.shortcuts import render
from rest_framework import generics
import copies

from copies.models import Copy, LoandBook
from copies.serializers import LoandSerializer
from django.shortcuts import get_object_or_404
from users.models import User
from users.permissions import IsColaborator, IsStudentAble
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class LoandView(generics.ListCreateAPIView):
    serializer_class = LoandSerializer
    permission_classes = [IsAuthenticated, IsStudentAble]
    lookup_url_kwarg = "user_id"

    def get_queryset(self):
        return LoandBook.objects.filter(users_id=self.request.user)

    def perform_create(self, serializer):
        pk = self.kwargs["user_id"]
        user = get_object_or_404(User, id=pk)
        copy_id = self.kwargs["copy_id"]
        copy = get_object_or_404(Copy, id=copy_id)

        serializer.save(users=user, copy=copy)


class LoandDetailView(generics.RetrieveAPIView):
    serializer_class = LoandSerializer
    lookup_url_kwarg = "user_id"
    permission_classes = [IsAuthenticated, IsColaborator]
    queryset = LoandBook.objects.all()
