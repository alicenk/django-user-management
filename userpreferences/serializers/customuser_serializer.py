# userpreferences/serializers/customuser_serializer.py
from rest_framework import serializers
from userpreferences.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active',
                  'date_joined')
