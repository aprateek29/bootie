from django.shortcuts import render, redirect
from .admin import UserCreationForm, UserChangeForm
from django.contrib.auth import logout, authenticate, login

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('/')