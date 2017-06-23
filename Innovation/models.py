from django.db import models
from taggit.managers import TaggableManager


class Collaborator(models.Model):
    name = models.CharField(blank=True, max_length=150)
    _lowername = models.CharField(blank=True, max_length=150)

    def __str__(self):
        return self.name

class Project(models.Model):
    objectives = models.CharField(blank=True,max_length=150)
    buckets = models.CharField(blank=True, max_length=150)
    title = models.CharField(blank=True,max_length=150)
    description = models.TextField(blank=True, max_length=500)
    tags = TaggableManager(blank=True)
    collaborators = models.ManyToManyField(Collaborator, blank=True)

    def __str__(self):
        return self.title
