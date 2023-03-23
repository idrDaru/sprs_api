from django.db import models
from api.models.parking_providers import ParkingProvider
import uuid


class ParkingSpace(models.Model):
    class Meta:
        db_table = 'parking_spaces'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    provider = models.ForeignKey(ParkingProvider, on_delete=models.CASCADE)
    address_line_one = models.CharField(max_length=255)
    address_line_two = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255)
    state_province = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    parking_space_number = models.IntegerField()
    image_file_name = models.CharField(max_length=255)
    image_file_path = models.CharField(max_length=255)