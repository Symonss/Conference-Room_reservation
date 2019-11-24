from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from mainapp.models import User, Reservation
from datetimepicker.widgets import DateTimePicker

class Admin_uSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ( 'full_name','email','username', 'password1', 'password2', )
        
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin_u = True
        if commit:
            user.save()
        return user
    
class ManagerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ( 'full_name','email','username', 'password1', 'password2', )
        
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_manager = True
        if commit:
            user.save()
        return user
    
class UserSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ( 'department_name','username', 'password1', 'password2', )
        
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_user = True
        if commit:
            user.save()
        return user

