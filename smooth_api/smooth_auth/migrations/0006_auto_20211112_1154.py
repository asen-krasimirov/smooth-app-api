# Generated by Django 3.2.9 on 2021-11-12 09:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smooth_auth', '0005_auto_20211112_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smoothsession',
            name='expiry_data',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 12, 11, 54, 28, 623859)),
        ),
        migrations.AlterField(
            model_name='smoothsession',
            name='set_data',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 12, 11, 54, 28, 623859)),
        ),
    ]
