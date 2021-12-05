from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

JOB_TYPE_CHOICES = [
    ('FT', 'Full-time'),
    ('PT', 'Part-time'),
]

HIRING_STATUS_CHOICES = [
    ('AH', 'Activity Hiring'),
    ('PH', 'Passive Hiring'),
]


class Job(models.Model):
    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        max_length=100,
    )

    description = models.CharField(
        max_length=2500,
    )

    type = models.CharField(
        max_length=2,
        choices=JOB_TYPE_CHOICES,
    )

    status = models.CharField(
        max_length=2,
        choices=HIRING_STATUS_CHOICES,
    )


class AppliedJob(models.Model):
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
