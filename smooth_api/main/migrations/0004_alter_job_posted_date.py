# Generated by Django 3.2.9 on 2021-12-10 14:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_job_posted_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='posted_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 10, 16, 56, 41, 239385)),
        ),
    ]