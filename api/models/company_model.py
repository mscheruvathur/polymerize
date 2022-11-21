from .main_model import MainModel
from djongo import models

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