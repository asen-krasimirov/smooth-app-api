# Generated by Django 3.2.9 on 2021-12-08 07:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('smooth_auth', '0021_alter_smoothsession_expiry_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smoothsession',
            name='expiry_data',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 8, 7, 31, 11, 239333, tzinfo=utc)),
        ),
    ]
