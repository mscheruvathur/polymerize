from .main_model import MainModel
from djongo import models
from .company_model import Company

class Admin(MainModel):

    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=100, blank=True)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True)

    objects = models.DjongoManager()

    def __str__(self):
        return f"{self.username} - {self.id}"
