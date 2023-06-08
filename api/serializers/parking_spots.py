from rest_framework import serializers
from api.models.parking_spots import ParkingSpot

class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = '__all__'
        
        extra_kwargs = {
            'name': {"required": False, "allow_null": True},
            'type': {"required": False, "allow_null": True},
            'status': {"required": False, "allow_null": True},
            'position': {"required": False, "allow_null": True},
        }
