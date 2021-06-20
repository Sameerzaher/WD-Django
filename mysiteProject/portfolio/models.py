from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.title
