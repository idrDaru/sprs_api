from rest_framework import serializers
from api.models.parking_spaces import ParkingSpace
from api.models.parking_providers import ParkingProvider
from api.serializers.parking_locations import ParkingLocationSerializer
from api.serializers.parking_layouts import ParkingLayoutSerializer
from api.serializers.parking_providers import ParkingProviderSerializer

class ParkingProviderRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        serializer = ParkingProviderSerializer(value)
        return serializer.data
    
    def to_internal_value(self, data):
        try:
            user = ParkingProvider.objects.get(id=data['id'])
            return user
        except ParkingProvider.DoesNotExist:
            raise serializers.ValidationError(
                'User Not Found'
            )

class ParkingSpaceSerializer(serializers.ModelSerializer):
    provider = ParkingProviderRelatedField(queryset=ParkingProvider.objects.all())
    parkinglayout_set = ParkingLayoutSerializer(many=True)
    parkinglocation_set = ParkingLocationSerializer(many=True)

    class Meta:
        model = ParkingSpace
        fields = '__all__'