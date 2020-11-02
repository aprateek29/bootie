from django.shortcuts import render, redirect
from .admin import UserCreationForm, UserChangeForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            messages.info(request, f"New account created for {username}")
            form.save()
            return redirect('/')
        else:
            messages.error(request, "Some error occurred")
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def logout_view(request):
    logout(request)
    messages.info(request, f"Logged Out")
    return redirect('/')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form":form})
