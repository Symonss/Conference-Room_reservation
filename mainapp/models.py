from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import datetime
import random
from django.urls import reverse

"""
Users of the system:
    1. The admin, Admin will have all rights and previlages
    2. Conference room managers, will be responsible for the rooms 
    3.Normal users, Responsible only for bookings
I abstact the user class and add Booloan flugs to separate user types such 
that when user is registering they are either set as true or False.by 
default a user is NU.
"""

class Organization(models.Model):
    org_name = models.CharField(max_length = 100)
    is_paid = models.BooleanField(default= False)
    location = models.CharField(max_length= 100)
    
    def __str__(self):
        return self.org_name

class User(AbstractUser):
    is_admin_u = models.BooleanField(default=False)
    is_manager = models.BooleanField(default = False)
    is_user =models.BooleanField(default = False)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    org_owner = models.ForeignKey(Organization,on_delete=models.CASCADE, null = True, blank = True, related_name='my_Porgs')
    organization_in = models.ForeignKey(Organization,on_delete=models.CASCADE, null = True, blank = True, related_name='my_orgs')


class Halls(models.Model):
    hall_name = models.CharField(max_length= 100)
    hall_abr = models.CharField(max_length= 100)
    hall_manager = models.ForeignKey(User,on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.hall_name

    