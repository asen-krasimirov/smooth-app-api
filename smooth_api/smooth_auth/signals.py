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


@receiver(post_save, sender=BusinessProfile)
def check_if_business_profile_is_complete(sender, instance, created, **kwargs):
    if instance.is_complete:
        return

    fields = [
        instance.name == '',
        instance.about_info == '',
        instance.icon_image == ''
    ]

    if not any(fields):
        instance.is_complete = True
        instance.save()


@receiver(post_save, sender=ApplicantProfile)
def check_if_applicant_profile_is_complete(sender, instance, created, **kwargs):
    if instance.is_complete:
        return

    fields = [
        instance.first_name == '',
        instance.last_name == '',
        instance.about_info == '',
        instance.icon_image == '',
    ]

    if not any(fields):
        instance.is_complete = True
        instance.save()
