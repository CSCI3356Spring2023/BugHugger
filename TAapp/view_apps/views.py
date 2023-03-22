from django.shortcuts import render, redirect

from .models import Course
from datetime import datetime
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
    if request.method == "POST":
        professor_name = request.POST['name']
        title = request.POST['course_name']
        description = request.POST['course_description']
        c = Course(course_title = title, description_text = description, professor_text = professor_name, pub_date = datetime.now(), course_id = "NEW", has_meetings = True, has_discussion = True, section = 1, num_sections = 4, num_office_hours = 6, num_tas = 4)
        c.save()
        return redirect('/view_apps/')
    else:
        return render(request, 'view_apps/create_course.html')

def apply(request):
    latest_course_list = Course.objects.all()
    context = {'latest_course_list': latest_course_list}
    return render(request, 'view_apps/apply.html', context)
