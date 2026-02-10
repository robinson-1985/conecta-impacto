from django.db import models
from django.conf import settings
from apps.skills.models import Skill


class Project(models.Model):

    STATUS_CHOICES = [
        ("OPEN", "Open"),
        ("IN_PROGRESS", "In Progress"),
        ("CLOSED", "Closed"),
    ]

    organization = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects_created"
    )

    title = models.CharField(max_length=255)
    description = models.TextField()

    required_skills = models.ManyToManyField(
        Skill,
        blank=True,
        related_name="projects"
    )

    hours_per_week = models.PositiveIntegerField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="OPEN"
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
