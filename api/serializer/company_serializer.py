from rest_framework import serializers
from api.models import Company


class CompanyCreationSerializer(serializers.ModelSerializer) :

    class Meta:
        model = Company
        fields = [ 'name', 'slug', 'first_name', 'last_name', 'phone', 'email', 'designation' ]