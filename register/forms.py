from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    
    VACCINE_CHOICES = [
        ('pfizer', 'Pfizer'),
        ('moderna', 'Moderna'),
        ('johnson', 'Johnson & Johnson'),
        ('astrazeneca', 'AstraZeneca'),
    ]


    GOVERNORATE_CHOICES = [
        ('Cairo', 'Cairo'),
        ('Alexandria', 'Alexandria'),
        ('Luxor', 'Luxor'),
        ('Aswan', 'Aswan'),
        ('Dakahlia', 'Dakahlia'),
        ('Damietta', 'Damietta'),
    ]
    
    name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=20)
    national_id = forms.CharField(max_length=20)
    vaccine_type = forms.ChoiceField(choices=VACCINE_CHOICES)
    governrate = forms.ChoiceField(choices=GOVERNORATE_CHOICES)
    date_of_birth = forms.DateField()
    

    
    class Meta:
        model = User
        fields = ('username', 'name', 'phone_number','national_id', 'password1', 'password2')