# Generated by Django 3.2.9 on 2021-11-16 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smooth_auth', '0013_alter_smoothsession_expiry_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smoothsession',
            name='expiry_data',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 16, 18, 33, 51, 301583)),
        ),
    ]
