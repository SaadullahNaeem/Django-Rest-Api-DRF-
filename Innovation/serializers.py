from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)
from .models import *


class ProjectSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Project
        fields = '__all__'
        depth = 1

class CollaboratorSerializer(serializers.ModelSerializer):
      class Meta:
        model = Collaborator
        fields = '__all__'
