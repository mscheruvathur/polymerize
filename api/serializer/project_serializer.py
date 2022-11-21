from rest_framework import serializers
from api.models import Project
from datetime import datetime, timedelta, timezone


class ProjectCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = [  'name', 'slug', 'title', 'keywords', 'description', 'company' ]
