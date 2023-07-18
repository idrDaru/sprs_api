from rest_framework import serializers
from api.models.parking_spaces import ParkingSpace
from api.models.parking_providers import ParkingProvider
from api.models.parking_layouts import ParkingLayout
from api.models.parking_locations import ParkingLocation
from api.models.bookings import Booking
from api.serializers.parking_locations import ParkingLocationSerializer
from api.serializers.parking_layouts import ParkingLayoutSerializer
from api.serializers.parking_providers import ParkingProviderSerializer
from api.serializers.parking_space_booking import ParkingSpaceBookingSerializer

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
        
class ParkingLayoutRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        serializer = ParkingLayoutSerializer(value)
        return serializer.data
    
    def to_internal_value(self, data):
        try:
            parking_layout = ParkingLayout.objects.get(id=data['id'])
            return parking_layout
        except ParkingLayout.DoesNotExist:
            raise serializers.ValidationError(
                'Parking Layout Not Found'
            )

class ParkingLocationRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        serializer = ParkingLocationSerializer(value)
        return serializer.data
    
    def to_internal_value(self, data):
        try:
            parking_location = ParkingLocation.objects.get(id=data['id'])
            return parking_location
        except ParkingLocation.DoesNotExist:
            raise serializers.ValidationError(
                'Parking Location Not Found'
            )

class BookingRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        serializer = ParkingSpaceBookingSerializer(value)
        return serializer.data
    
    def to_internal_value(self, data):
        try:
            booking = Booking.objects.get(id=data['id'])
            return booking
        except Booking.DoesNotExist:
            raise serializers.ValidationError(
                'Booking Not Found'
            )

class ParkingSpaceSerializer(serializers.ModelSerializer):
    provider = ParkingProviderRelatedField(queryset=ParkingProvider.objects.all(), required=False)
    parkinglayout_set = ParkingLayoutRelatedField(queryset=ParkingLayout.objects.all(), many=True, required=False)
    parkinglocation_set = ParkingLocationRelatedField(queryset=ParkingLocation.objects.all(), many=True, required=False)
    booking_set = BookingRelatedField(queryset=Booking.objects.all(), many=True, required=False)

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