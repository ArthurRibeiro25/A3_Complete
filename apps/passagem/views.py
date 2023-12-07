from django.shortcuts import render
from .models import PassagensClass
from rest_framework import viewsets
from .serializer import PassagensClassSerializer
import psycopg2

# Create your views here.

class PassagensClassViewSet(viewsets.ModelViewSet):
    queryset = PassagensClass.objects.all()
    serializer_class = PassagensClassSerializer



