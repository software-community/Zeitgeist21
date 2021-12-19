
from django import forms
from django.forms.widgets import Widget
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CampusAmbassadorRegistrationDetailsForm(forms.ModelForm):
    class Meta:
        model = RegistrationDetail
        fields = ['collegeName', 'mobileNumber', 'whyInterested',
            'pastExperience']
        widgets = {
            'collegeName': forms.TextInput(attrs={'class': 'collegeName form'}),
            'mobileNumber' : forms.TextInput(attrs={'class': 'mobileNumber form'}),
            'whyInterested' : forms.TextInput(attrs={'class': 'whyInterested form'}),
            'pastExperience' : forms.TextInput(attrs={'class': 'pastExperience form'}),
        }
        