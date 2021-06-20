from django.shortcuts import render
from .models import Project


def project_list(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'portfolio/project_list.html', context)
