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
class User(AbstractUser):
    is_admin_u = models.BooleanField(default=False)
    is_manager = models.BooleanField(default = False)
    is_user =models.BooleanField(default = False)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    