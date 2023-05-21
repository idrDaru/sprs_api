from rest_framework import serializers
from api.models.parking_providers import ParkingProvider
from api.models.users import User
from api.serializers.users import UserSerializer

class UserRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        serializer = UserSerializer(value)
        return serializer.data
    
    def to_internal_value(self, data):
        try:
            user = User.objects.get(id=data['id'])
            return user
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User Not Found'
            )

class ParkingProviderSerializer(serializers.ModelSerializer):
    user = UserRelatedField(queryset=User.objects.all(), many=False, required=False)

    class Meta:
        model = ParkingProvider
        fields = '__all__'

        extra_kwargs = {
            'name': {"required": False, "allow_null": True},
            'address_line_one': {"required": False, "allow_null": True},
            'address_line_two': {"required": False, "allow_null": True},
            'city': {"required": False, "allow_null": True},
            'state_province': {"required": False, "allow_null": True},
            'country': {"required": False, "allow_null": True},
            'postal_code': {"required": False, "allow_null": True},
        }