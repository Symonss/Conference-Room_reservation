from django.contrib.auth import login
from django.shortcuts import redirect
from ..forms import Admin_uSignUpForm
from django.shortcuts import render
from ..models import User, Organization
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
        organization = Organization.objects.get(pk=self.kwargs['pk'])
        user.org_owner = organization
        user.organization_in = organization
        user = form.save()
        login(self.request, user)
        return redirect('a_home')

def home(request):
    return render(request,'app/admin_home.html',{})
    
class OrganizationCreateView(CreateView):
    model = Organization
    fields = '__all__'
    template_name = 'app/Organization_form.html'
    def form_valid(self, form):
        org = form.save(commit=False)
        org.save()
        return redirect('admin_signup', org.pk)