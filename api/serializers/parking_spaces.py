from rest_framework import serializers
from api.models.parking_spaces import ParkingSpace
from api.models.parking_providers import ParkingProvider
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

    class Meta:
        model = ParkingSpace
        fields = (
            'id',
            'address_line_one',
            'address_line_two',
            'city',
            'state_province',
            'country',
            'postal_code',
            'parking_space_number',
            'image_file_name',
            'image_file_path',
            'provider',
        )