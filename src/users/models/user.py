
from django.db import models
from django.contrib.auth.models import AbstractUser
from base_services.models import AutoTimeStampedModel, TinyIntegerField
from users.constants.constants import AccountType


class User(AbstractUser, AutoTimeStampedModel):
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.CharField(max_length=255, unique=True)
    account_type = TinyIntegerField(default=AccountType.FREE, null=True, db_index=True)
    buy_premium_date = models.DateTimeField(null=True)
    used_tokens = models.IntegerField(max_length=10000, null=True, default=0)

    class Meta:
        db_table = "users"