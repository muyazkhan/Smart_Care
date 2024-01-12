from django.shortcuts import render
from rest_framework import viewsets
from .models import Doctor,specialization,designation,AvailableTime,review
from .serializers import doctorserializers,designationserializers,AvailableTimeserializers,reviewserializers,specializationserializers
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission
from rest_framework import filters, pagination


class DesignatioViewSet(viewsets.ModelViewSet):
    queryset = designation.objects.all()
    serializer_class = designationserializers

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set
    
class AvailableTimeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeserializers
    filter_backends = [AvailableTimeForSpecificDoctor]

class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1 # items per page
    page_size_query_param = page_size
    max_page_size = 100

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = doctorserializers
    pagination_class = DoctorPagination

class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = specialization.objects.all()
    serializer_class = specializationserializers

class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = review.objects.all()
    serializer_class = reviewserializers
