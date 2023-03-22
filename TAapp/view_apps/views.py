from django.shortcuts import render, redirect

from .models import Course, App
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
        c = Course(course_title = title, description_text = description, professor_text = professor_name, pub_date = datetime.now(), course_id = id, has_meetings = True, has_discussion = True, section = section, num_sections = num_sections, num_office_hours = oh, num_tas = ta, time_text = time)
        c.save()
        return redirect('/view_apps/')
    else:
        return render(request, 'view_apps/create_course.html')

def apply(request):
    if request.method == "POST":
        course_id = request.POST['courseID']
        student_name = request.POST['name']
        eagle_id = request.POST['eagleID']
        office_hours = request.POST['office_hours']
        major = request.POST['major']
        why_ta = request.POST['course_description']
        c = App(course_id, student_name, eagle_id, office_hours, major, why_ta)
        c.save()
        return redirect('/view_apps/')
    courseID = request.GET['courseID'] if 'courseID' in request.GET else "NULL"
    # latest_course_list = Course.objects.all()
    context={"courseID": courseID}
    return render(request, 'view_apps/apply.html', context)
