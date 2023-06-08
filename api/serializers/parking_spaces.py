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
    provider = ParkingProviderRelatedField(queryset=ParkingProvider.objects.all(), required=False)
    parkinglayout_set = ParkingLayoutSerializer(many=True, required=False)
    parkinglocation_set = ParkingLocationSerializer(many=True, required=False)

    class Meta:
        model = ParkingSpace
        fields = '__all__'
        extra_kwargs = {
            'name': {"required": False, "allow_null": True},
            'address_line_one': {"required": False, "allow_null": True},
            'address_line_two': {"required": False, "allow_null": True},
            'city': {"required": False, "allow_null": True},
            'state_province': {"required": False, "allow_null": True},
            'country': {"required": False, "allow_null": True},
            'postal_code': {"required": False, "allow_null": True},
            'parking_space_number': {"required": False, "allow_null": True},
            'image_download_url': {"required": False, "allow_null": True},
            'is_active': {"required": False, "allow_null": True},
        }