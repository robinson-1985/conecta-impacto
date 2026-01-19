from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, OrganizationProfile, VolunteerProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if not created:
        return
    
    if created:
        if instance.is_volunteer:
            VolunteerProfile.objects.create(user=instance)
            
        elif instance.is_organization:
            OrganizationProfile.objects.create(
                user=instance,
                name=instance.email
            )
