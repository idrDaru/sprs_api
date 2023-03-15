from django.db import models
from api.models.users import User
import uuid

class ParkingUser(models.Model):
    class Meta:
        db_table = 'parking_users'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True)
