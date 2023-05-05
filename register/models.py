from django.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    national_id = models.CharField(max_length=20)
    VACCINE_CHOICES = [
        ('pfizer', 'Pfizer'),
        ('moderna', 'Moderna'),
        ('johnson', 'Johnson & Johnson'),
        ('astrazeneca', 'AstraZeneca'),
    ]
    vaccine_type = models.CharField(max_length=100, choices=VACCINE_CHOICES)
    GOVERNORATE_CHOICES = [
        ('CAI', 'Cairo'),
        ('ALX', 'Alexandria'),
        ('LUX', 'Luxor'),
        ('ASN', 'Aswan'),
        ('MANS', 'Mansoura'),
        ('DUM', 'Damietta'),
    ]
    governrate = models.CharField(max_length=100, choices=GOVERNORATE_CHOICES)



