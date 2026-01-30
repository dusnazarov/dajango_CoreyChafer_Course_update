from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # print(username)
            # print(form.cleaned_data)
            # You might want to redirect to a success page here
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    # print(form)
    return render(request, 'users/register.html', {'form': form})