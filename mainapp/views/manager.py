from django.contrib.auth import login
from django.shortcuts import redirect
from ..forms import ManagerSignUpForm
from django.shortcuts import render
from ..models import User, Reservation, Halls
# from django.utils.decorators import method_decorator
# from ..decorators import department_required
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)


class ManagerSignUpView(CreateView):
    model = User
    form_class = ManagerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'manager'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user = form.save()
        # login(self.request, user)
        return redirect('a_home')
def home(request):
    hall_in = Halls.objects.get(hall_manager = request.user.pk)
    reservations = Reservation.objects.filter(hall = hall_in.pk).order_by('-start_date_time')


    return render(request,'manager/manager_home.html',{'reservations':reservations,'hall_in':hall_in})