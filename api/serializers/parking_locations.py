from rest_framework import serializers
from api.models.parking_locations import ParkingLocation

class ParkingLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingLocation
        fields = '__all__'