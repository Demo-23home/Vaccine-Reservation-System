from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from .models import UserProfile
from datetime import datetime, timedelta
import random


from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 != password2:
                form.add_error('password2', 'Passwords do not match.')
                return render(request, 'register/register.html', {'form': form})

            national_id = form.cleaned_data['national_id']
            phone_number = form.cleaned_data['phone_number']

            # Check length of national ID
            if len(national_id) != 14:
                error_message = 'National ID must be exactly 14 characters.'
                form.add_error('national_id', error_message)
                return render(request, 'register/register.html', {'form': form})

            # Check length of phone number
            if len(phone_number) != 11:
                error_message = 'Phone number must be exactly 11 digits.'
                form.add_error('phone_number', error_message)
                return render(request, 'register/register.html', {'form': form})

            user = form.save()
            profile = UserProfile(user=user, name=form.cleaned_data['name'], phone_number=phone_number, national_id=national_id, vaccine_type=form.cleaned_data['vaccine_type'], governrate=form.cleaned_data['governrate'])
            profile.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register/register.html', {'form': form})




from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'register/login.html', {'form': form})



from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if 'future_date' not in request.session:
        today = datetime.now().date()
        max_days = (today.replace(day=1) + timedelta(days=92)).replace(day=1) - today
        future_date = today + timedelta(days=random.randint(1, max_days.days))
        request.session['future_date'] = future_date.strftime('%Y-%m-%d')
    else:
        future_date = datetime.strptime(request.session['future_date'], '%Y-%m-%d').date()
    return render(request, 'register/profile.html', {'user_profile': user_profile,
                                                     'date':future_date,
                                                     })





def home(request):
    return render(request,'register/home.html')