# Generated by Django 3.2.9 on 2021-12-10 14:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('smooth_auth', '0025_alter_smoothsession_expiry_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smoothsession',
            name='expiry_data',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 10, 14, 56, 41, 238385, tzinfo=utc)),
        ),
    ]