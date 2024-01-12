from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views
router = DefaultRouter()
router.register(r'list', views.DoctorViewSet)
router.register(r'Specialization', views.SpecializationViewSet)
router.register(r'Designatio', views.DesignatioViewSet)
router.register(r'AvailableTime', views.AvailableTimeViewSet)
router.register(r'Review', views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]