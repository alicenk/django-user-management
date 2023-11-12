# userpreferences/serializers/userpreference_serializer.py
from rest_framework import serializers
from userpreferences.models import UserPreference
from userpreferences.serializers import CustomUserSerializer, SectorSerializer


class UserPreferenceSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    sector = SectorSerializer()

    class Meta:
        model = UserPreference
        fields = ('id', 'user', 'sector')
