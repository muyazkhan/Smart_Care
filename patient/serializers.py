from rest_framework import serializers
from .models import Patient
from django.contrib.auth.models import User


class patient(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)

    class Meta:
        model = Patient
        fields = '__all__'
        # fields = ['name', 'phone', 'problem']


class registrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password', 'confirm_password']

    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']

        if password != password2:
            raise serializers.ValidationError(
                {'error': "Password And Confirm-Password doesn't Match"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'error': "Email alreday Exist Try another email"})
        account = User(username=username, email=email)
        account.set_password(password)
        account.is_active = False  # user account deactive when open account
        account.save()
        return account
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)