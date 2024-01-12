from django.shortcuts import render
from rest_framework import viewsets
from .models import Contact_Us
from .serializers import contact_us

class contuctUsViewSet(viewsets.ModelViewSet):
    queryset = Contact_Us.objects.all()
    serializer_class = contact_us
# Create your views here.
