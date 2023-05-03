from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics

from copies.models import LoandBook

# Create your views here.


class LoanView(generics.ListCreateAPIView):
    queryset = LoandBook.objects.all()
