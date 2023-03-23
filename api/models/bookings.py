from django.db import models
from api.models.parking_users import ParkingUser
from api.models.parking_spaces import ParkingSpace
import uuid

class Booking(models.Model):
    class Meta:
        db_table = 'bookings'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(ParkingUser, on_delete=models.CASCADE)
    parking_space = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE)
    is_purchased = models.BooleanField(default=False)
    date = models.DateField()
    time_from = models.TimeField()
    time_to = models.TimeField()
