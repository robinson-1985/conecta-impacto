from django.contrib import admin
from apps.projects.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description')
