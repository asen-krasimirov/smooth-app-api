# Generated by Django 3.2.9 on 2021-11-12 09:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smooth_auth', '0004_smoothsession'),
    ]

    operations = [
        migrations.AddField(
            model_name='smoothsession',
            name='expiry_data',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 12, 11, 53, 48, 681603)),
        ),
        migrations.AddField(
            model_name='smoothsession',
            name='set_data',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 12, 11, 53, 48, 681603)),
        ),
    ]
