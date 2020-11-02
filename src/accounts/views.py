from django.shortcuts import render, redirect
from .admin import UserCreationForm, UserChangeForm
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.info(request, f"New account created for {username}")
            form.save()
            return redirect('/')
        else:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 == password2:
                if len(password1) < 6:
                    messages.error(request, "Passwords too small")
                else:
                    if get_user_model().objects.exists(email=email):
                        messages.error(request, "User with this email exits atleast 6 char")
            else:
                messages.error(request, "Passwords does not match")

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
