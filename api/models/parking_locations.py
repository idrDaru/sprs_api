from django.db import models
from api.models.parking_spaces import ParkingSpace
import uuid

class ParkingLocation(models.Model):
    class Meta:
        db_table = 'parking_locations'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parking_space = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE)
    location_path = models.CharField(max_length=255, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()