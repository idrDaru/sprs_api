from rest_framework import serializers
from api.models.parking_layouts import ParkingLayout
from api.serializers.parking_spots import ParkingSpotSerializer

class ParkingLayoutSerializer(serializers.ModelSerializer):
    parkingspot_set = ParkingSpotSerializer(many=True)
    
    class Meta:
        model = ParkingLayout
        fields = '__all__'
