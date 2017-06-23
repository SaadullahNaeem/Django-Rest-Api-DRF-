from django import forms
from taggit.forms import TagWidget

from Innovation.models import Project, Collaborator


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title', 'objectives', 'buckets', 'description', 'tags', 'collaborators')
        widgets = {
            'tags': TagWidget(),
        }


class CollaborativeForm(forms.ModelForm):

    class Meta:
        model = Collaborator
        fields = ('name', '_lowername')