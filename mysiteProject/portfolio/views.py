from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


def project_list(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'portfolio/project_list.html', context)


def create_project(request):

    if request.method == 'GET':
        return render(request, 'portfolio/project_create.html', {'form': ProjectForm()})
    else:
        try:
            form = ProjectForm(request.POST)
            form.save()
            return redirect('portfolio:project_list')
        except ValueError:
            return render(request, 'portfolio/project_create.html', {'form': ProjectForm(), 'error': 'Bad data passed in. Try again.'})


class ProjectCreateView(CreateView):
    model = Project
    fields = ['title', 'description']
