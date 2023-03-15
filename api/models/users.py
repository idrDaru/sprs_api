from django.db import models
import uuid

class User(models.Model):
    class Meta:
        db_table = 'users'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    profile_file_name = models.CharField(max_length=255, null=True)
    profile_file_path = models.CharField(max_length=255, null=True)
    type = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)