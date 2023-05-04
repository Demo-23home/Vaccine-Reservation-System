from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=20)
    national_id = forms.CharField(max_length=20)
    
    class Meta:
        model = User
        fields = ('username', 'name', 'phone_number', 'national_id', 'password1', 'password2')