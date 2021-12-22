"""zeitgeist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from allauth.account.views import logout

urlpatterns = [
    path('', RedirectView.as_view(pattern_name = 'mainPage'), name='home'),
    path('z22-admin-iitrpr/', admin.site.urls),
    # path('api/', include('api.urls')),
    path('TSP/', include('TSP.urls')),
    path('campus_ambassador/', include('CA.urls')),

    # Login/Logout
    # Use /acounts/google/login/?next=/<url> to login
    # Use /acounts/logout/?next=/<url> to logout
    path('accounts/', include('allauth.socialaccount.providers.google.urls')),
    path('accounts/logout/', logout, name="logout"),

]
