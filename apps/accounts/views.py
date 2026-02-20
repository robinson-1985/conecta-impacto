from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.projects.models import Application

@login_required
def dashboard(request):
    applications = Application.objects.filter(volunteer=request.user).order_by('-created_at')

    return render(request, 'accounts/dashboard.html', {
        'applications': applications
    })
