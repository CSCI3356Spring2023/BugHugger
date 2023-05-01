from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from login.forms import ProfProfileForm, StudProfileForm

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

def user_create_student(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        profile = StudProfileForm(request.POST)
        if form.is_valid() and profile.is_valid():
            f = form.save()
            p = profile.save(commit=False)
            user_group = Group.objects.get(name='Student')
            f.groups.add(user_group)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            p.user=user
            p.save()
            login(request, user)
            return redirect('/view_apps/')
    else:
        form = UserCreationForm()
        profile = StudProfileForm()
    return render(request, 'registration/create_student.html', {
        'form': form,
        'profile': profile
    })
    
def user_create_professor(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        profile = ProfProfileForm(request.POST)
        if form.is_valid() and profile.is_valid():
            f = form.save()
            p = profile.save(commit=False)
            user_group = Group.objects.get(name='Professor')
            f.groups.add(user_group)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            p.user=user
            p.save()
            login(request, user)
            return redirect('/view_apps/')
    else:
        form = UserCreationForm()
        profile = ProfProfileForm()
    return render(request, 'registration/create_professor.html', {
        'form': form,
        'profile': profile
    })