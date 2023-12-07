from django.shortcuts import render
from .models import AvioesClass
from rest_framework import viewsets
from .serializer import AvioesClassSerializer

# Create your views here.

class AvioesClassViewSet(viewsets.ModelViewSet):
    queryset = AvioesClass.objects.all()
    serializer_class = AvioesClassSerializer  
