# Generated by Django 3.2.9 on 2021-11-30 15:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smooth_auth', '0015_alter_smoothsession_expiry_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantprofile',
            name='background_image',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='applicantprofile',
            name='icon_image',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='background_image',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='icon_image',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='smoothsession',
            name='expiry_data',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 30, 17, 32, 34, 890172)),
        ),
    ]
