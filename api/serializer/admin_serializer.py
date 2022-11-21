from rest_framework import serializers
from api.models import Admin
from django.contrib.auth.hashers import make_password
from datetime import datetime, timezone,timedelta

class AdminRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['first_name', 'last_name', 'email', 'password']

    
    def create (self):
        data = self.validated_data
        data['password'] = make_password(self.data['password'])
        admin = Admin(
            **data,
            adminname= self.data['email'].split('@')[0],
            date_joined=datetime.now(tz=timezone.utc),
            user_type = 'ADMIN'
            )
        admin.save()
        return admin



class AdminLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = Admin
        fields = ['password', 'email']

        
class AdminUpdationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255)
    class Meta:
        model = Admin
        fields = ['first_name', 'last_name', 'employeename', 'email', 'phone']