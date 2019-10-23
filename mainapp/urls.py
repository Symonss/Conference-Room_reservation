from django.contrib import admin
from django.urls import include, path
from mainapp.views import manager, admin_u, user,main

urlpatterns = [
    path('', main.home, name= 'home'),
    path('mangers/home', manager.home, name = 'm_home'),
    path('admins/home', admin_u.home, name = 'a_home'),
    path('user/home', user.home, name = 'u_home'),
    path('reservation/new/', main.CreatesView.as_view(), name='reservation_new'),
    path('room/create', main.HallCreateView.as_view(), name = 'hall_c'),

    path('reservation/<int:pk>/', main.reservation_detail, name='reservation_detail'),
    path('Reservation/<pk>/complete/', main.reservation_complete, name='reservation_complete'),

  
]
