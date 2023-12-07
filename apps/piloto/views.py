from django.shortcuts import render
from .models import PilotosClass
from rest_framework import viewsets
from .serializer import PilotoClassSerializer

# Create your views here.

class PilotosClassViewSet(viewsets.ModelViewSet):
    queryset = PilotosClass.objects.all()
    serializer_class = PilotoClassSerializer 