from django.urls import path,include
from django.urls.resolvers import URLPattern
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.mainPage, name='mainPage'),
    path('register/',views.registerPage,name='register'),
    path('contact_us/',views.contactUs,name='contact'),
    path('about_us/',views.aboutUs,name='about')
]
