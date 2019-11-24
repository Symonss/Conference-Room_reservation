from django.contrib.auth import login
from django.shortcuts import redirect
from ..forms import UserSignUpForm
from django.shortcuts import render
from ..models import User, Reservation
# from django.utils.decorators import method_decorator
# from ..decorators import department_required
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)



class UserSignUpView(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'user'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user = form.save()
        login(self.request, user)
        return redirect('u_home')
    
def home(request):
    myreservations = Reservation.objects.filter(created_by = request.user.pk)
    return render(request, 'user/user_home.html',{'myreservations':myreservations})
    

