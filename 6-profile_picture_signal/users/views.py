from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()          
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('users-login')
    else:
        form = UserRegisterForm()
    # print(form)
    return render(request, 'users/register.html', {'form': form})


def logout_view(request):
    logout(request)
    
    return render(request, 'users/logout.html')

@login_required(login_url='users-login') 
def profile(request):
    return render(request, 'users/profile.html')