# Generated by Django 3.2.5 on 2023-02-08 03:16

import base_services.models.custom_type
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20230102_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account_type',
            field=base_services.models.custom_type.TinyIntegerField(db_index=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='buy_premium_date',
            field=models.DateTimeField(null=True),
        ),
    ]
