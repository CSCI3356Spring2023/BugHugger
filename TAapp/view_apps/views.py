from django.shortcuts import render

from .models import Course
from django.contrib.auth.models import User

def is_student(user):
    return user.groups.filter(name='Student').exists()
def is_professor(user):
    return user.groups.filter(name='Professor').exists()

def index(request):
    user = request.user
    if is_student(user):
        latest_course_list = Course.objects.all()
        context = {'latest_course_list': latest_course_list}
        return render(request, 'view_apps/student.html', context)
    elif is_professor(user):
        latest_course_list = Course.objects.all()
        context = {'latest_course_list': latest_course_list,}
        return render(request, 'view_apps/professor.html', context)
    else:
        return render(request, 'view_apps/professor.html')

def create_course(request):
    latest_course_list = Course.objects.all()
    context = {'latest_course_list': latest_course_list}
    return render(request, 'view_apps/create_course.html', context)

def apply(request):
    latest_course_list = Course.objects.all()
    context = {'latest_course_list': latest_course_list}
    return render(request, 'view_apps/apply.html', context)
