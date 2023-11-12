# userpreferences/serializers/sector_serializer.py
from rest_framework import serializers
from userpreferences.models import Sector

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ('id', 'name')
