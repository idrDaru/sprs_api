from rest_framework import serializers
from api.models.parking_layouts import ParkingLayout
from api.serializers.parking_spots import ParkingSpotSerializer

class ParkingLayoutSerializer(serializers.ModelSerializer):
    parkingspot_set = ParkingSpotSerializer(many=True, required=False)
    
    class Meta:
        model = ParkingLayout
        fields = '__all__'

        extra_kwargs = {
            'car_spot_number': {"required": False, "allow_null": True},
            'motorcycle_spot_number': {"required": False, "allow_null": True},
            'car_price': {"required": False, "allow_null": True},
            'motorcycle_price': {"required": False, "allow_null": True},
            'position': {"required": False, "allow_null": True},
        }
