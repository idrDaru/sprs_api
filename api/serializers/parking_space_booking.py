from rest_framework import serializers
from api.models.bookings import Booking

class ParkingSpaceBookingSerializer(serializers.ModelSerializer):
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