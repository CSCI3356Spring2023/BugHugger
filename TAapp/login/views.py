from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm 

from .models import User

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request)
        if user is not None:
            login(request, user)
            return redirect('view_apps')
        else:
            return redirect('login')
    return render(request, 'registration/login.html', {})

def user_create(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('view_apps/index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/create.html', {
        'form' : form,
    })