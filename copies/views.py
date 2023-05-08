import uuid
from django.shortcuts import render
from rest_framework import generics, status
from books.models import Book
from copies.models import Copy, LoandBook
from copies.serializers import LoanSerializer
from django.shortcuts import get_object_or_404
from users.models import User
from users.permissions import IsColaborator, IsStudentAble
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response


class LoanView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated, IsStudentAble]
    lookup_url_kwarg = "user_id"
    queryset = LoandBook.objects.all()

    def perform_create(self, serializer):
        pk = self.request.user.id
        user = get_object_or_404(User, id=pk)

        book_id = self.request.data.get("book_id")
        book = get_object_or_404(Book, id=book_id)

        copy = (
            Copy.objects.filter(
                books_id=book.id,
                is_available=True,
            )
            .order_by("id")
            .first()
        )

        if not copy:
            return Response(
                {"error": "Copy does not exist or is not available"}, status=404
            )

        copy.is_available = False
        copy.save()

        serializer.save(users=user, copy=copy)


class LoandDetailView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = LoanSerializer
    lookup_url_kwarg = "user_id"
    permission_classes = [IsAuthenticated, IsColaborator]
    queryset = LoandBook.objects.all()


class CheckoutBook(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = LoanSerializer

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
