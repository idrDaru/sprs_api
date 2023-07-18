from django.db import models
from django.contrib.postgres.fields import ArrayField
from api.models.parking_users import ParkingUser
from api.models.parking_spaces import ParkingSpace
import uuid

class Booking(models.Model):
    class Meta:
        db_table = 'bookings'
        ordering = ['-time_from']

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(ParkingUser, on_delete=models.CASCADE)
    parking_space = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE)
    is_purchased = models.BooleanField(default=False)
    time_from = models.DateTimeField()
    time_to = models.DateTimeField()
    total_car = models.IntegerField(null=True)
    total_motorcycle = models.IntegerField(null=True)
    total_price = models.FloatField()
    parking_spot = ArrayField(models.UUIDField())
    is_active = models.BooleanField(default=False)
    is_expired = models.BooleanField(default=False)
