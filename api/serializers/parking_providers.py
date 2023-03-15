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
    user = UserRelatedField(queryset=User.objects.all(), many=False)

    class Meta:
        model = ParkingProvider
        fields = (
            'id',
            'name',
            'address_line_one',
            'address_line_two',
            'city',
            'state_province',
            'country',
            'postal_code',
            'user',
        )