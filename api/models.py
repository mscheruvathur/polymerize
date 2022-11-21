# # from django.db import models

# # Create your models here.
# from api.models.admin_model import Admin
# from api.models.administrator_model import Administrator
# from api.models.company_model import Company
# from api.models.main_model import MainModel
# from api.models.user_model import User, UserToken
from djongo import models


class MainModel(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    added_by = models.CharField(max_length=255, null=True, default="Anonymous")

    def active_inactive(self):
        self.is_active = not self.is_active
        self.save()

    def update_added_by(self, added_by):
        self.added_by = added_by
        self.save()

    class Meta:
        abstract = True

class Company(MainModel):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    designation = models.CharField(max_length=255)
    date_joined = models.DateTimeField()
    title = models.CharField(max_length=255, default="", blank=True)
    keywords = models.TextField(max_length=255, default="", blank=True)
    description = models.TextField(max_length=255, default="", blank=True)
    objects = models.DjongoManager()

    def __str__(self):
        return self.slug

class Project(MainModel) : 
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255, default="", blank=True)
    keywords = models.TextField(max_length=255, default="", blank=True)
    description = models.TextField(max_length=255, default="", blank=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    objects = models.DjongoManager()

    def __str__(self):
        return self.slug

class Administrator(MainModel):

    adminname = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=100, blank=True)
    user_type = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)
    company = models.OneToOneField('Company', on_delete=models.CASCADE, null=True)

    objects = models.DjongoManager()

    def __str__(self):
        return f"{self.adminname} - {self.id}"

class Admin(MainModel):

    adminname = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=255)
    user_type = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)
    company = models.OneToOneField('Company', on_delete=models.CASCADE, null=True)

    objects = models.DjongoManager()

    def __str__(self):
        return f"{self.adminname} - {self.id}"


        
class Employee(MainModel):
    company = models.OneToOneField('Company', on_delete=models.CASCADE, null=True)
    employeename = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_type = models.CharField(max_length=100)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(blank=True, null=True)

    objects = models.DjongoManager()

    def __str__(self):
        return f"{self.employeename} - {self.id}"


class AuthToken(MainModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, null=True)
    administrator = models.ForeignKey(Administrator, on_delete=models.CASCADE, null=True)
    access_token = models.TextField()
    refresh_token = models.TextField()
    is_revoked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_id} - {self.user_token_id}"


class AuthCode(MainModel):

    auth_code = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    admin = models.ForeignKey(Admin,on_delete=models.CASCADE,null=True)
    administrator = models.ForeignKey(Administrator,on_delete=models.CASCADE,null=True)
    is_used = models.BooleanField(default=False)
    expiration = models.DateTimeField(blank=True, null=True)