from django.db import models
from api.models.users import User
import uuid

class ParkingProvider(models.Model):
    class Meta:
        db_table = 'parking_providers'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address_line_one = models.CharField(max_length=255)
    address_line_two = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255)
    state_province = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
