from django.db.models.base import Model
from .models import Project
from django.forms import ModelForm


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']
