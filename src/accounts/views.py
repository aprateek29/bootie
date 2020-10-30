from django.shortcuts import render
from .admin import UserCreationForm, UserChangeForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})