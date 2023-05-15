from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(user=user, name=form.cleaned_data['name'], phone_number=form.cleaned_data['phone_number'], national_id=form.cleaned_data['national_id'],vaccine_type = form.cleaned_data['vaccine_type'],governrate=form.cleaned_data['governrate'])
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
    return render(request, 'register/profile.html', {'user_profile': user_profile})





def home(request):
    return render(request,'register/home.html')