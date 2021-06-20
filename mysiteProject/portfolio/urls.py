from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.project_list, name='project_list'),
]
