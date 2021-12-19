from django.db import models
from users.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from phonenumber_field.modelfields import PhoneNumberField

class RegistrationDetail(models.Model):
    collegeName = models.CharField(max_length=200,null=False,verbose_name='College Name')
    campusAmbassadorCode = models.CharField(max_length=15, verbose_name='CA Code', unique=True)
    mobileNumber = PhoneNumberField(null=False, blank=False, verbose_name='Mobile Number', region='IN')
    whyInterested = models.TextField(verbose_name='Why do you want to be a Campus Ambassador?')
    pastExperience = models.TextField(verbose_name='Do you have any past experience related to this? If yes, then please share your experience')
    user = models.ForeignKey(User,on_delete=CASCADE,null=True)

    class Meta:
        verbose_name_plural = 'Registration details'

    def __str__(self):
        return str(self.campusAmbassadorCode)

