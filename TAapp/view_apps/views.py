from django.shortcuts import render

from .models import Course
from login.models import User


def index(request):
    users = User.objects.all()
    latest_course_list = Course.objects.all()
    context = {'latest_course_list': latest_course_list, 'users': users}
    return render(request, 'view_apps/index.html', context)

def create_course(request):
    users = User.objects.all()
    latest_course_list = Course.objects.all()
    context = {'latest_course_list': latest_course_list, 'users': users}
    return render(request, 'view_apps/create_course.html', context)
