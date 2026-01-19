from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, OrganizationProfile, VolunterProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_volunteer:
            VolunterProfile.objects.create(user=instance)
        elif instance.is_organization:
            OrganizationProfile.objects.create(user=instance)
