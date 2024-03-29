from rest_framework import serializers
from api.models.bookings import Booking
from api.models.parking_users import ParkingUser
from api.models.parking_spaces import ParkingSpace
from api.serializers.parking_users import ParkingUserSerializer
from api.serializers.parking_spaces import ParkingSpaceSerializer

class ParkingUserRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        serializer = ParkingUserSerializer(value)
        return serializer.data
    
    def to_internal_value(self, data):
        try:
            user = ParkingUser.objects.get(id=data['id'])
            return user
        except ParkingUser.DoesNotExist:
            raise serializers.ValidationError(
                'User Not Found'
            )

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

class BookingSerializer(serializers.ModelSerializer):
    user = ParkingUserRelatedField(queryset=ParkingUser.objects.all(), many=False, required=False)
    parking_space = ParkingSpaceRelatedField(queryset=ParkingSpace.objects.all(), many=False, required=False)
    
    class Meta:
        model = Booking
        fields = '__all__'

        extra_kwargs = {
            'is_purchased': {"required": False, "allow_null": True},
            'time_from': {"required": False, "allow_null": True},
            'time_to': {"required": False, "allow_null": True},
            'total_car': {"required": False, "allow_null": True},
            'total_motorcycle': {"required": False, "allow_null": True},
            'total_price': {"required": False, "allow_null": True},
            'parking_spot': {"required": False, "allow_null": True},
        }