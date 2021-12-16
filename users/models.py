from django.contrib.auth.models import AbstractUser
from django.db import models
from random import randint

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

def gen_new_zcode():
  code = "Z22#"
  code += str(randint(100000,999999))
  return code

def get_new_zcode():
  code = None
  while 1:
    code = gen_new_zcode()
    if len(User.objects.all().filter(zcode=code))==0:
      break
  return code

def set_zcode(sender, instance, **kwargs):
    if instance.zcode=="":
        zcode = get_new_zcode()
        instance.zcode = zcode

models.signals.pre_save.connect(set_zcode, sender=User)

def set_participation(sender, instance, **kwargs):
  if instance.participation=="":
    instance.participation = "[]"

models.signals.pre_save.connect(set_participation, sender=User)
