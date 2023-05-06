from django.shortcuts import render
from rest_framework import generics, status
from copies.models import Copy, LoandBook
from copies.serializers import LoandSerializer
from django.shortcuts import get_object_or_404
from users.models import User
from users.permissions import IsColaborator, IsStudentAble
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response


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

        copy.is_available = False
        copy.save()

        serializer.save(users=user, copy=copy)


class LoandDetailView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = LoandSerializer
    lookup_url_kwarg = "user_id"
    permission_classes = [IsAuthenticated, IsColaborator]
    queryset = LoandBook.objects.all()


class CheckoutBook(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = LoandSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        user = get_object_or_404(User, id=user_id)
        copy_id = self.request.data.get("copy_id")
        loan = LoandBook.objects.filter(copy_id=copy_id, users_id=user.id)
        return loan

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if queryset.exists():
            loan_book = queryset.first()

            if loan_book.is_return:
                return Response({"error": "Book is returned"})
            copy = loan_book.copy
            copy.is_available = True
            copy.save()

            loan_book.is_return = True
            loan_book.save()

            serializer = self.serializer_class(loan_book)

            return Response(serializer.data)

        return Response({"error": "Loan not found"}, status=status.HTTP_404_NOT_FOUND)
