from django.db import models

from django.shortcuts import reverse


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio:project_list')
