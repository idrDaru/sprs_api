from django.db import models
from api.models.parking_spaces import ParkingSpace
import uuid

class ParkingLayout(models.Model):
    class Meta:
        db_table = 'parking_layouts'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parking_space = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE)
    car_spot_number = models.IntegerField(null=True)
    motorcycle_spot_number = models.IntegerField(null=True)
    position = models.CharField(max_length=255)