from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from ..models import User
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.utils import timezone


def home(request):
    return render(request,'mainapp/home.html',{})
    
