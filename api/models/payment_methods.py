from django.db import models
from api.models.parking_users import ParkingUser
import uuid

class PaymentMethod(models.Model):
    class Meta:
        db_table = 'payment_methods'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(ParkingUser, on_delete=models.CASCADE)
    card_number = models.IntegerField()
    expires_year = models.IntegerField()
    expires_month = models.IntegerField()
    cvv = models.IntegerField()
    type = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True)