# Generated by Django 3.2.9 on 2021-11-30 15:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smooth_auth', '0016_auto_20211130_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smoothsession',
            name='expiry_data',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 30, 17, 33, 20, 901648)),
        ),
    ]