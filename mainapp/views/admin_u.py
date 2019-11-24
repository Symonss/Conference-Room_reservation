from django.contrib.auth import login
from django.shortcuts import redirect
from ..forms import Admin_uSignUpForm
from django.shortcuts import render
from ..models import User, Reservation, Halls
# from django.utils.decorators import method_decorator
# from ..decorators import department_required
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)



class Admin_uSignUpView(CreateView):
    model = User
    form_class = Admin_uSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin_u'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user = form.save()
        login(self.request, user)
        return redirect('a_home')

def home(request):
    reservations = Reservation.objects.all()
    managers = User.objects.filter(is_manager = True)
    departments = User.objects.filter(is_user = True)
    halls = Halls.objects.all()
    context = {
            'reservations': reservations,
            'managers': managers,
            'halls': halls,
            'departments':departments,
        }
    
    return render(request,'admin/admin_home.html', context)
    
