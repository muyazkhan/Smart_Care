from django.shortcuts import render
from rest_framework import viewsets
from .models import Service
from .serializers import service

class serviceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = service
# Create your views here.
