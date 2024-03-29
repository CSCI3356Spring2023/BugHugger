from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from .models import Prof_profile, Stud_profile, Admin_profile
from .forms import ProfProfileForm, StudProfileForm, AdminProfileForm

def login_user(request):
    student_group, created = Group.objects.get_or_create(name='Student')
    professor_group, created = Group.objects.get_or_create(name='Professor')
    admin_group, created = Group.objects.get_or_create(name='Admin')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('view_apps')
        else:
            return redirect('login')
    return render(request, 'registration/login.html', {})

def user_create_student(request):
    student_group, created = Group.objects.get_or_create(name='Student')
    professor_group, created = Group.objects.get_or_create(name='Professor')
    admin_group, created = Group.objects.get_or_create(name='Admin')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        profile = StudProfileForm(request.POST)
        if form.is_valid() and profile.is_valid():
            user = form.save()
            user_group = Group.objects.get(name='Student')
            user.groups.add(user_group)
            user.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                profile_obj = profile.save(commit=False)
                profile_obj.user = user
                profile_obj.save()
                return redirect('/view_apps/')
    else:
        form = UserCreationForm()
        profile = StudProfileForm()
    return render(request, 'registration/create_student.html', {
        'form': form,
        'profile': profile
    })

def user_create_professor(request):
    student_group, created = Group.objects.get_or_create(name='Student')
    professor_group, created = Group.objects.get_or_create(name='Professor')
    admin_group, created = Group.objects.get_or_create(name='Admin')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        profile = ProfProfileForm(request.POST)
        if form.is_valid() and profile.is_valid():
            user = form.save()
            user_group = Group.objects.get(name='Professor')
            user.groups.add(user_group)
            user.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                profile_obj = profile.save(commit=False)
                profile_obj.user = user
                profile_obj.save()
                return redirect('/view_apps/')
    else:
        form = UserCreationForm()
        profile = ProfProfileForm()
    return render(request, 'registration/create_professor.html', {
        'form': form,
        'profile': profile
    })

def user_create_admin(request):
    student_group, created = Group.objects.get_or_create(name='Student')
    professor_group, created = Group.objects.get_or_create(name='Professor')
    admin_group, created = Group.objects.get_or_create(name='Admin')
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        profile = ProfProfileForm(request.POST)
        if form.is_valid() and profile.is_valid():
            user = form.save()
            user_group = Group.objects.get(name='Admin')
            user.groups.add(user_group)
            user.is_staff = True
            user.is_admin = True
            user.is_superuser = True
            user.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                profile_obj = profile.save(commit=False)
                profile_obj.user = user
                profile_obj.save()
                return redirect('/view_apps/')
    else:
        form = UserCreationForm()
        profile = ProfProfileForm()
    return render(request, 'registration/create_admin.html', {
        'form': form,
        'profile': profile
    })
