from rest_framework import serializers
from api.models import Employee
from django.contrib.auth.hashers import make_password
from datetime import datetime, timezone,timedelta

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'password']

    
    def create (self):
        data = self.validated_data
        data['password'] = make_password(self.data['password'])
        user = Employee(
            **data,
            employeename= self.data['email'].split('@')[0],
            date_joined=datetime.now(tz=timezone.utc),
            user_type = 'EMPLOYEE'
            )
        user.save()
        return user



class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = Employee
        fields = ['password', 'email']

        
class UserUpdationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255)
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'employeename', 'email', 'phone']