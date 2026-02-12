from django.shortcuts import render
from .models import Project


def project_list(request):
    projects = Project.objects.filter(status="OPEN", is_active=True)

    return render(
        request,
        "projects/project_list.html",
        {"projects": projects}
    )