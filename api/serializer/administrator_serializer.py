from rest_framework import serializers
from api.models import Administrator
from django.contrib.auth.hashers import make_password
from datetime import datetime, timezone,timedelta

class AdministratorRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = ['first_name', 'last_name', 'email', 'password']

    
    def create (self):
        data = self.validated_data
        data['password'] = make_password(self.data['password'])
        admin = Administrator(
            **data,
            adminname= self.data['email'].split('@')[0],
            date_joined=datetime.now(tz=timezone.utc),
            user_type = 'ADMINISTRATOR'
            )
        admin.save()
        return admin

