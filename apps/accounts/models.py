from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.skills.models import Skill


class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    
    is_volunteer = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class VolunterProfile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='volunteer_profile'
    )
    
    bio = models.TextField(blank=True, null=True)
    avaliability_hours_per_week = models.PositiveIntegerField(null=True, blank=True)
    skills = models.ManyToManyField(
        Skill, 
        blank=True, 
        related_name='volunteers'
    )
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Voluntário:{self.user.username}"


class OrganizationProfile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='organization_profile'
    )
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
