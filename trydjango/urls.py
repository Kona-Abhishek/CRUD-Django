"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from profiles.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('getProfiles',getProfiles,name='getProfiles'),
    path('getting_profiles',getting_profiles,name='getting_profiles'),
    path('',getting_profiles,name='home'),
    path('create',create,name='create'),
    path('insert',insert,name='insert'),
    path('delete/<int:pk>',delete,name="delete"),
    path('get_profile/<int:ID>',get_profile,name='get_profile'),
    path('update',update,name="update")
]
