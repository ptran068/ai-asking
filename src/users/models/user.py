
from django.db import models
from django.contrib.auth.models import AbstractUser
from base_services.models import AutoTimeStampedModel


class User(AbstractUser, AutoTimeStampedModel):
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "users"