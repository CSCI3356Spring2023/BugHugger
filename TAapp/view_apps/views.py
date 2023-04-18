from django.shortcuts import render, redirect
from django.contrib.auth import logout #Added by Aidan
from .models import Course, App
from datetime import datetime
from django.core.mail import send_mail
from django.contrib.auth.models import User

def is_student(user):
    return user.groups.filter(name='Student').exists()
def is_professor(user):
    return user.groups.filter(name='Professor').exists()

def index(request):
    user = request.user
    if is_student(user):
        course_list = Course.objects.all()
        context = {'course_list': course_list}
        return render(request, 'view_apps/student.html', context)
    elif is_professor(user):
        course_list = Course.objects.all().filter(assigned_to_email = user.username)
        context = {'course_list': course_list}
        return render(request, 'view_apps/professor.html', context)
    else:
        course_list = Course.objects.all().filter(assigned_to_email=user.username)
        context = {'course_list': course_list}
        return render(request, 'view_apps/professor.html', context)

def create_course(request):
    if request.method == "POST":
        email = request.user.username
        professor_name = request.POST['name']
        title = request.POST['course_name']
        description = request.POST['course_description']
        id = request.POST['course_id']
        time = request.POST['time_text']
        section = request.POST['section']
        num_sections = request.POST['num_sections']
        oh = request.POST['office_hours']
        ta = request.POST['TAs']
        meet = request.POST['meet']
        disc = request.POST['disc']
        meet_val = True
        disc_val = False
        if meet == 'yes':
            meet_val = True
        if disc == 'yes':
            disc_val = True

        c = Course(assigned_to_email = email, time_text=time, course_title=title, description_text=description,
                   professor_text=professor_name, pub_date=datetime.now(), course_id=id, has_meetings=meet_val,
                   has_discussion=disc_val, section=section, num_sections=num_sections, num_office_hours=oh, num_tas=ta)
        c.save()
        send_mail(
            'Successfully Created Course',
            title,
            'forbushs@bc.edu',
            [email + '@bc.edu'],
            fail_silently=False,
        )
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
        why_ta = request.POST['why_ta']
        #print(App.objects.values())
        if App.objects.filter(eagle_id=eagle_id).count()>4: return render(request, 'view_apps/too_many_apps.html')
        c = App(course_id, student_name, eagle_id, office_hours, major, why_ta)
        c.save()
        return redirect('/view_apps/')
    courseID = request.GET['courseID'] if 'courseID' in request.GET else 9999
    # latest_course_list = Course.objects.all()
    context={"courseID": courseID}
    return render(request, 'view_apps/apply.html', context)


#Function added by Aidan
def logoff(request):
    logout(request)
    return redirect('login')
