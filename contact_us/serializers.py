from rest_framework import serializers
from .models import Contact_Us


class contact_us(serializers.ModelSerializer):
    class Meta:
        model = Contact_Us
        fields = '__all__'
        # fields = ['name', 'phone', 'problem']
