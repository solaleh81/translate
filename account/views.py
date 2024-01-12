# views.py
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


def home(request):
    return render(request, 'account/index.html')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if not username:
                messages.error( 'ttttttttttttttttttttttttttt')
            else:
                user = form.save()
                login(request, user)
                return redirect('home')
        else:
            print(form.errors)


    else:
        form = UserCreationForm()

    return render(request, 'account/signup.html', {'form': form})
