from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
import datetime
import random
from django.urls import reverse


class User(AbstractUser):
    is_admin_u = models.BooleanField(default=False)
    is_manager = models.BooleanField(default = False)
    is_user =models.BooleanField(default = False)
    full_name = models.CharField(max_length=100, null = True, blank = True, default = 'No Name')
    email = models.EmailField(max_length=254, null = True, blank =True)
    department_name = models.CharField(max_length=100,  null = True, blank = True)

    def __str__(self):
        return self.full_name

class Halls(models.Model):
    hall_name = models.CharField(max_length= 100)
    hall_abr = models.CharField(max_length= 100)
    hall_manager = models.OneToOneField(User,on_delete=models.CASCADE, related_name ='managing')

        
    def __str__(self):
        return self.hall_name

class Reservation(models.Model):
    title = models.CharField(max_length = 100)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    hall = models.ForeignKey(Halls, on_delete = models.CASCADE)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)
    is_accepted = models.BooleanField(default = False)
    is_complete = models.BooleanField(default = False)
    is_current = models.BooleanField(default = True)

    def get_absolute_url(self):
        return reverse('home')
    

    