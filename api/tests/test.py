from django.db import models

class User(models.Model):
    class Meta:
        db_table = 'users'
        