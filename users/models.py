from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(max_length=256)
    mobile = models.CharField(max_length=10)
    active = models.BooleanField(null=True,default=False)
    zcode = models.CharField(max_length=10)

    def __str__(self):
        return self.username