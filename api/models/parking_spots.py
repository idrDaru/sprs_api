from django.db import models
from api.models.parking_layouts import ParkingLayout
import uuid

class ParkingSpot(models.Model):
    class Meta:
        db_table = 'parking_spots'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    layout = models.ForeignKey(ParkingLayout, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.IntegerField()
    status = models.BooleanField()
    position = models.CharField(max_length=255)
    price = models.FloatField()