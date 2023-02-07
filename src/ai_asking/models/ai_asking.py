#
# from django.db import models
# from base_services.models import AutoTimeStampedModel, TinyIntegerField
# from email_store.constants.constants import EmailStatus
#
#
# class EmailStoreModel(AutoTimeStampedModel):
#     id = models.AutoField(primary_key=True)
#     email = models.CharField(max_length=255, db_index=True, unique=True)
#     # email = models.EmailField(max_length=255, db_index=True, unique=True)
#     status = TinyIntegerField(default=EmailStatus.UNSUBSCRIBED, db_index=True)
#
#     class Meta:
#         db_table = "email_store"
