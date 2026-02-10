from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.conf import settings
from .managers import UserManager
from apps.skills.models import Skill


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    role = models.CharField(
        max_length=20,
        choices=[
            ("VOLUNTEER", "Volunteer"),
            ("ORGANIZATION", "Organization"),
        ]
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    @property
    def is_volunteer(self):
        return self.role == "VOLUNTEER"

    @property
    def is_organization(self):
        return self.role == "ORGANIZATION"
    

class VolunteerProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="volunteer_profile"
    )

    bio = models.TextField(blank=True, null=True)
    availability_hours_per_week = models.PositiveIntegerField(null=True, blank=True)

    skills = models.ManyToManyField(
        Skill,
        blank=True,
        related_name="volunteers"
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Voluntário: {self.user.email}"


class OrganizationProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="organization_profile"
    )

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
