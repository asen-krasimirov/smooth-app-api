# Generated by Django 3.2.9 on 2021-11-12 11:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smooth_auth', '0009_auto_20211112_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessprofile',
            name='about_info',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='name',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='sub_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='smoothsession',
            name='expiry_data',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 12, 13, 59, 6, 894300)),
        ),
    ]
