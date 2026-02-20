from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project, Application
from .forms import ApplicationForm
from .models import Project


@login_required
def apply_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if Application.objects.filter(project=project, volunteer=request.user).exists():
        messages.warning(request, 'Você já se candidatou para este projeto.')
        return redirect('project_detail', pk=pk)
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.project = project
            application.volunteer = request.user
            application.save()
            
            messages.success(request, 'Candidatura enviada com sucesso!')
            return redirect('project_detail', pk=pk)
    else:
        form = ApplicationForm()
    
    return render(request, 'projects/apply_project.html', {
        'form': form,
        'project': project
    })


def project_list(request):
    projects = Project.objects.all().order_by('-id')

    return render(request, 'projects/project_list.html', {
        'projects': projects
    })


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    return render(request, 'projects/project_detail.html', {
        'project': project
    })
