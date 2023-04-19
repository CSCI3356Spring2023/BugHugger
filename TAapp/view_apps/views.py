from django.shortcuts import render, redirect
from django.contrib.auth import logout #Added by Aidan
from .models import Course, App
from datetime import datetime
from django.core.mail import send_mail
from login.models import Prof_profile, Stud_profile



def is_student(user):
    return user.groups.filter(name='Student').exists()
def is_professor(user):
    return user.groups.filter(name='Professor').exists()

def index(request):
    user = request.user
    if is_student(user):
        course_list = Course.objects.all()
        if App.objects.all().filter(user=user).exists():
            apps = App.objects.all().filter(user=user)
            applied_course_list = []
            for c in course_list:
                for a in apps:
                    if a.id in c.applications:
                        applied_course_list.append(c)

        else:
            apps = 0
        context = {'course_list': course_list,'apps': apps, 'applied_course_list': applied_course_list}
        return render(request, 'view_apps/student.html', context)
    elif is_professor(user):
        course_list = Course.objects.all().filter(assigned_to_email = user.username)
        context = {'course_list': course_list}
        return render(request, 'view_apps/professor.html', context)
    else:
        course_list = Course.objects.all().filter(assigned_to_email=user.username)
        context = {'course_list': course_list}
        return render(request, 'view_apps/professor.html', context)

def applications(request, id):
    user = request.user
    applications_id_list = Course.objects.all().get(course_id=id).applications.split()
    applications_list = []
    for a in applications_id_list:
        if App.objects.all().filter(id = a).exists():
            applications_list.append(App.objects.all().get(id = a))
    context = {"applications_list": applications_list, "id": id}
    return render(request, 'view_apps/applications.html', context)
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

def apply(request, id):
    MAX_APPLICATIONS = 5
    if request.method == "POST":
        user=request.user
        if App.objects.filter(user=user).exists():
            c = App.objects.filter(user=user).count()
            num_uses = c + 1
            course_id = id
            office_hours = request.POST['office_hours']
            why_ta = request.POST['why_ta']
            if num_uses > MAX_APPLICATIONS: return render(request, 'view_apps/too_many_apps.html')
            else:
                #IMPORTANT: Assuming course_id is unique
                c = App(user=user, num_uses = num_uses, office_hours=office_hours, why_ta=why_ta)
                current_apps = Course.objects.get(course_id=course_id).applications
                current_apps += " " + c.id
                Course.objects.filter(course_id = course_id).update(applications = current_apps)
                c.save()
        else:
            num_uses = 1
            user = request.user
            course_id = id
            office_hours = request.POST['office_hours']
            why_ta = request.POST['why_ta']
            c = App(user=user, office_hours=office_hours, why_ta=why_ta, num_uses=num_uses)
            # IMPORTANT: Assuming course_id is unique
            current_apps = Course.objects.get(course_id=course_id).applications
            current_apps += " " + c.id
            Course.objects.filter(course_id=course_id).update(applications=current_apps)
            c.save()
        return redirect('/view_apps/')
    context={"id": id}
    return render(request, 'view_apps/apply.html', context)

#Function added by Aidan
def logoff(request):
    logout(request)
    return redirect('login')
