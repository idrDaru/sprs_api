from rest_framework import serializers
from api.models.parking_locations import ParkingLocation
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

class ParkingLocationSerializer(serializers.ModelSerializer):
    parking_space = ParkingSpaceRelatedField(queryset=ParkingSpace.objects.all(), many=False)
    
    class Meta:
        model = ParkingLocation
        fields = (
            'id',
            'parking_space',
            'location_path',
            'latitude',
            'longitude',
        )
