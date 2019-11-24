from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from ..models import User,Halls
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from bootstrap_datepicker_plus import DateTimePickerInput
from django.urls import reverse
from django.views import generic
from ..models import Reservation
from django.http import HttpResponseRedirect


def home(request):
    return render(request,'app/landing.html',{})


class HallCreateView(CreateView):
    model = Halls
    fields = ('hall_name','hall_abr','hall_manager')
    template_name = 'app/reserve.html'

    def form_valid(self, form):
        hall = form.save(commit=False)
        hall.save()
        # messages.success(self.request, 'Ticket Succesfully Created!')
        return redirect('a_home')
    

class CreatesView(generic.edit.CreateView):
    model = Reservation
    fields = ['title','start_date_time','end_date_time','hall','created_by']
    template_name = 'app/reserve.html'

    def get_form(self):
        form = super().get_form()
        form.fields['start_date_time'].widget = DateTimePickerInput()
        form.fields['end_date_time'].widget = DateTimePickerInput()
        return form

    
def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    return render(request, 'app/reservation_detail.html', {'reservation': reservation})


def reservation_complete(request, pk ,):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.is_complete = True
    reservation.save()
    # ticket.mark_closed(closer)
    return redirect('reservation_detail', pk=pk)

