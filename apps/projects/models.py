from django.db import models
from apps.skills.models import Skill
from apps.accounts.models import OrganizationProfile


class Project(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Aberto'),
        ('IN_PROGRESS', 'Em andamento'),
        ('COMPLETED', 'Finalizado'),
    ]
    
    organization = models.ForeignKey(
        OrganizationProfile, 
        on_delete=models.CASCADE, 
        related_name='projects'
    )
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    required_skills = models.ManyToManyField(
        Skill,
        related_name='projects',
    )
    
    is_remote = models.BooleanField(default=False)
    
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='OPEN'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
