from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from smooth_api.smooth_auth.models import BusinessProfile, ApplicantProfile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_business:
            BusinessProfile.objects.create(user=instance)
        else:
            ApplicantProfile.objects.create(user=instance)
