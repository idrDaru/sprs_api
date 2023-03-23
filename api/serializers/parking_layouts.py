from rest_framework import serializers
from api.models.parking_layouts import ParkingLayout
from api.models.parking_spaces import ParkingSpace
from api.serializers.parking_spaces import ParkingSpaceSerializer

class ParkingSpaceRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        serializer = ParkingSpaceSerializer(value)
        return serializer.data
    
    def to_internal_value(self, data):
        try:
            parking_space = ParkingSpace.objects.get(id=data['id'])
            return parking_space
        except ParkingSpace.DoesNotExist:
            raise serializers.ValidationError(
                'Parking Space Not Found'
            )

class ParkingLayoutSerializer(serializers.ModelSerializer):
    parking_space = ParkingSpaceRelatedField(queryset=ParkingSpace.objects.all(), many=False)

    class Meta:
        model = ParkingLayout
        fields = (
            'id',
            'parking_space',
            'car_spot_number',
            'motorcycle_spot_number',
            'position',
        )
