from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(max_length=256)
    mobile = models.CharField(max_length=10)
    active = models.BooleanField(null=True,default=False)
    zcode = models.CharField(max_length=10)
    college = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    participation = models.CharField(max_length=5000, blank=True)
    total = models.IntegerField(null=True)

    def __str__(self):
        return self.username