from django.conf import settings
from djongo import models
from .company_model import Company

from .main_model import MainModel

POINT_HEAD = settings.POINT_HEAD

class User(MainModel):
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=100, blank=True)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(blank=True, null=True)

    objects = models.DjongoManager()

    def __str__(self):
        return f"{self.username} - {self.id}"


class UserToken(MainModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    access_token = models.TextField()
    refresh_token = models.TextField()
    ip_address = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    is_revoked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_id} - {self.user_token_id}"
