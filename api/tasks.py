from __future__ import absolute_import, unicode_literals

from celery import shared_task
from api.models.bookings import Booking
from api.models.parking_spots import ParkingSpot
from api.serializers.parking_spots import ParkingSpotSerializer
from api.serializers.bookings import BookingSerializer
from django.utils import timezone
import pytz

@shared_task
def check_is_booking_activated():
    """
    Function to check if a booking should be activated
    """
    booking = Booking.objects.all()
    for value in booking:
        if compare_date(value.time_from) and value.is_expired != True and value.is_purchased == True:
            serializer = BookingSerializer(value, data={'is_active': True})
            if serializer.is_valid():
                serializer.save()
                continue
            return "Error"
        else:
            continue
        
    return "Success"

@shared_task
def check_is_booking_expired():
    """
    Function to check if a booking is expired
    """
    booking = Booking.objects.all()
    for value in booking:
        if value.is_purchased:
            if compare_date(value.time_to) and value.is_expired != True:
                serializer = BookingSerializer(value, data={'is_active': False, 'is_expired': True})
                if serializer.is_valid():
                    for value in serializer.data['parking_spot']:
                        parking_spot = ParkingSpot.objects.get(pk=value)
                        parking_spot_serializer = ParkingSpotSerializer(parking_spot, data={'status': True})
                        if parking_spot_serializer.is_valid():
                            parking_spot_serializer.save()
                    serializer.save()
                    continue
                return "Error"
            else:
                continue

    return "Success"

def compare_date(target):
    tmp_time = timezone.now()
    utc8 = pytz.timezone('Asia/Shanghai')
    current_datetime = tmp_time.astimezone(utc8).replace(second=0, microsecond=0, tzinfo=None)

    target_datetime = target.replace(second=0, microsecond=0, tzinfo=None)

    return current_datetime == target_datetime
