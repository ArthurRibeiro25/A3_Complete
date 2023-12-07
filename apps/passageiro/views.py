from django.shortcuts import render
from .models import PassageirosClass
from rest_framework import viewsets
from .serializer import PassageirosClassSerializer

# Create your views here.

class PassageirosClassViewSet(viewsets.ModelViewSet):
    queryset = PassageirosClass.objects.all()
    serializer_class = PassageirosClassSerializer 
