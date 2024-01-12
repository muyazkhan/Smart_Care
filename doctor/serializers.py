from rest_framework import serializers
from .models import Doctor,designation,AvailableTime,review,specialization


class  doctorserializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    Designation = serializers.StringRelatedField(many=True)
    Specialization = serializers.StringRelatedField(many=True)
    available_time = serializers.StringRelatedField(many=True)
    class Meta:
        model =  Doctor
        fields = '__all__'

class  specializationserializers(serializers.ModelSerializer):
    class Meta:
        model =  specialization
        fields = '__all__'

class  designationserializers(serializers.ModelSerializer):
    class Meta:
        model =  designation
        fields = '__all__'

class  AvailableTimeserializers(serializers.ModelSerializer):
    class Meta:
        model =  AvailableTime
        fields = '__all__'

class  reviewserializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model =  review
        fields = '__all__'
