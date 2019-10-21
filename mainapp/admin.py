from django.contrib import admin
from .models import User,Halls,Reservation

admin.site.register(User)
admin.site.register(Halls)
admin.site.register(Reservation)
