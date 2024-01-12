from rest_framework import serializers
from .models import Service


class service(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        # fields = ['name', 'phone', 'problem']
