from django.shortcuts import render, redirect

from .models import Course
from datetime import datetime
from django.contrib.auth.models import User, Group

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
    if request.method == "POST":
        professor_name = request.POST['name']
        title = request.POST['course_name']
        description = request.POST['course_description']
        id = request.POST['course_id']
        time = request.POST['time_text']
        section = request.POST['section']
        num_sections = request.POST['num_sections']
        oh = request.POST['office_hours']
        ta = request.POST['TAs']
        c = Course(assigned_to = request.user, course_title = title, description_text = description, professor_text = professor_name, pub_date = datetime.now(), course_id = id, has_meetings = True, has_discussion = True, section = section, num_sections = num_sections, num_office_hours = oh, num_tas = ta)
        c.save()
        return redirect('/view_apps/')
    else:
        return render(request, 'view_apps/create_course.html')

def apply(request):
    latest_course_list = Course.objects.all()
    context = {'latest_course_list': latest_course_list}
    return render(request, 'view_apps/apply.html', context)
