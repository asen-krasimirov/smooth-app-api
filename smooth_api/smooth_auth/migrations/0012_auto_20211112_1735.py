# Generated by Django 3.2.9 on 2021-11-12 15:35

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models
import smooth_api.smooth_auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('smooth_auth', '0011_auto_20211112_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantprofile',
            name='education',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=150), default=smooth_api.smooth_auth.models.get_default_array, size=None),
        ),
        migrations.AlterField(
            model_name='applicantprofile',
            name='skills',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), default=smooth_api.smooth_auth.models.get_default_array, size=None),
        ),
        migrations.AlterField(
            model_name='smoothsession',
            name='expiry_data',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 12, 17, 35, 21, 372820)),
        ),
    ]