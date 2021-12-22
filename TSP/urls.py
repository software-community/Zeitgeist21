from django.contrib import admin
from django.urls import path,include
from django.views.decorators.csrf import csrf_exempt
from . import views
from django.contrib.auth import views as auth_views
app_name='TSP'

urlpatterns=[
    path('', views.TspHome,name='home'),
]
