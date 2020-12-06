from django.db import models
from django.utils import timezone


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(blank=True, unique=True, max_length=50)
    password = models.CharField(blank=True, max_length=50)

    class Meta:
        db_table = "users"
