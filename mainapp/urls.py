from django.contrib import admin
from django.urls import include, path
from mainapp.views import manager, admin_u, user,main

urlpatterns = [
    path('', main.home, name= 'home'),
   

  
]
