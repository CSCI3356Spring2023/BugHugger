from django.shortcuts import render, redirect
from django.contrib.auth import logout #Added by Aidan
from .models import Course, App, Semester
from datetime import datetime
from django.core.mail import send_mail
import random
from login.models import Prof_profile, Stud_profile
from django.conf import settings
from .forms import SemesterForm



#variables for course names
COURSE_NAMES = ["Computer Science I", "Computer Science II", "Object Oriented Design",
                "Algorithms", "Logic and Computation", "Randomness and Computation", "Robotics",
                "Computer Vision", "Natural Language Processing", "Web Application Development",
                "Computer Science I Honors", ]
#variables for course IDs
COURSE_IDS = ["CSCI1101", "CSCI1102", "CSCI3353", "CSCI3383", "CSCI2243", "CSCI2244", "CSCI3347",
                "CSCI3343", "CSCI3349", "CSCI2254","CSCI1103", ]
#variables for course times
COURSE_TIMES = ["MWF 9-9:50", "MWF 10-10:50", "MWF 11-11:50", "MWF 12-12:50", "MWF 1-1:50", "MWF 2-2:50",
                "MWF 3-3:50", "MWF 4-4:50", "MW 3-4:15","MW 4:30-6:15", "TTH 9-10:15", "TTH 10:30-11:45", "TTH 12-1:15",
                "TTH 1:30-2:45", "TTH 3-4:15", "TTH 4:30-5:45", ]

def is_student(user):
    return user.groups.filter(name='Student').exists()
def is_professor(user):
    return user.groups.filter(name='Professor').exists()
def is_admin(user):
    return user.groups.filter(name='Admin').exists()

def index(request):
    user = request.user
    if is_student(user):
        course_list = Course.objects.all()
        for c in course_list:
            if user.username in c.accepted_students:
                assigned_course = c
                context = {'assigned_course': assigned_course}
                return render(request, 'view_apps/student.html', context)
        if App.objects.all().filter(user=user).exists():
            apps = App.objects.all().filter(user=user)
            applied_course_list = []
            accepted_course_list = []
            for c in course_list:
                assigned_list = c.assigned_students.split()
                if user.username in assigned_list:
                    accepted_course_list.append(c)
                for a in apps:
                    if a.id in c.applications:
                        applied_course_list.append(c)
        else:
            apps = []
            applied_course_list = []
            accepted_course_list = []
        context = {'course_list': course_list,
                   'apps': len(apps),
                   'applied_course_list': applied_course_list,
                   'accepted_course_list': accepted_course_list,
                   }
        return render(request, 'view_apps/student.html', context)
    elif is_professor(user):
        course_list = Course.objects.all().filter(assigned_to_email = user.username)
        context = {'course_list': course_list}
        return render(request, 'view_apps/professor.html', context)
    elif is_admin(user):
        semesters = Semester.objects.all()
        course_list = Course.objects.all()
        context = {'semesters': semesters,
                   'courses': course_list}
        return render(request, 'view_apps/admin.html', context)
    else:
        course_list = Course.objects.all()
        context = {'course_list': course_list}

def view_courses(request, sem):
    courses = Course.objects.filter(semester = sem) 
    context = {'course_list': courses}
    return render(request, 'view_apps/view_courses.html',context)

def applications(request, id):
    user = request.user
    if is_professor(user):
        is_prof = True
    else: is_prof = False
    current_course = Course.objects.filter(course_id=id).first()
    applications_id_list = current_course.applications.split()
    assigned_students_string = current_course.assigned_students
    if assigned_students_string == "":
        assigned_students_list = []
        num_assigned = 0
    else:
        assigned_students_list = assigned_students_string.split()
        num_assigned = len(assigned_students_list)
    applications_list = []
    assigned_applications_list = []
    for a in applications_id_list:
        if App.objects.all().filter(id = a).exists():
            current_app = App.objects.all().get(id = a)
            if current_app.user.username in assigned_students_list:
                assigned_applications_list.append(current_app)
            elif current_app.is_visible: applications_list.append(current_app)
    context = {"applications_list": applications_list,
               "assigned_applications_list": assigned_applications_list,
               "id": id,
               "num_assigned": num_assigned,
               "assigned_students_list": assigned_students_list,
               "current_course": current_course,
               "is_prof": is_prof,}
    return render(request, 'view_apps/applications.html', context)

def assign_student(request, id, name):
    user = request.user
    current_course = Course.objects.all().get(course_id=id)
    applications_id_list = current_course.applications.split()
    assigned_students_string = current_course.assigned_students
    num_tas = current_course.num_tas

    if assigned_students_string == "":
        assigned_students_list = []
        num_assigned = 0
    else:
        assigned_students_list = assigned_students_string.split()
        num_assigned = len(assigned_students_list)
    if num_assigned == num_tas:
        return render(request, 'view_apps/too_many_assignments.html')
    elif name not in assigned_students_list and num_assigned < num_tas:
        for a in App.objects.all():
            if a.user.username == name:
                a.is_visible = False
                a.save()
        assigned_students_list.append(name)
        updated_assigned = " ".join(assigned_students_list)
        current_course.assigned_students = updated_assigned
        current_course.num_assigned = current_course.num_assigned + 1
        current_course.save()

        # Get the student's email from the Stud_profile model
        # student_email = Stud_profile.objects.get(user__username=name).email
        student_email = 'zhongpd@bc.edu'

        # Send an email to the student
        send_mail(
            f'Course TA Offer - {current_course.course_title}',
            f'Congrats, \n\nYou have been offered a TA position for the course {current_course.course_title}. Please log in to your account to accept or decline the offer.',
            settings.EMAIL_HOST_USER,
            ['zhongpd@bc.edu'],
            fail_silently=True,
        )

    return applications(request, id)


def accept(request, id):
    user = request.user
    current_course = Course.objects.all().get(course_id=id)
    assigned_list = current_course.assigned_students.split()
    accepted_list = current_course.accepted_students.split()
    if user.username in assigned_list and current_course.num_accepted < current_course.num_tas:
        assigned_list.remove(user.username)
        updated_assigned = " ".join(assigned_list)
        current_course.assigned_students = updated_assigned
        current_course.num_assigned = current_course.num_assigned - 1

        accepted_list.append(user.username)
        updated_accepted = " ".join(accepted_list)
        current_course.accepted_students = updated_accepted
        current_course.num_accepted = current_course.num_accepted + 1

        current_course.save()
        if current_course.num_accepted == current_course.num_tas:
            current_course.is_open = False
            current_course.save()
        for a in App.objects.all():
            if a.user.username == user.username:
                a.delete()
    return index(request)

def deny(request, id):
    user = request.user
    current_course = Course.objects.all().get(course_id=id)
    assigned_list = current_course.assigned_students.split()
    if user.username in assigned_list:
        assigned_list.remove(user.username)
        updated_assigned = " ".join(assigned_list)
        current_course.assigned_students = updated_assigned
        current_course.num_assigned = current_course.num_assigned - 1
        current_course.save()
        for a in App.objects.all():
            if a.user.username == user.username:
                a.is_visible = True
                a.save()
    return index(request)

def create_course(request):
    if request.method == "POST":
        user = request.user
        professor_profile = Prof_profile.objects.get(user=user)
        professor_email = professor_profile.email
        professor_name = f"{professor_profile.first_name} {professor_profile.last_name}"
        title = request.POST['course_name']
        description = request.POST['course_description']
        id = request.POST['course_id']
        time = request.POST['course_time']
        section = request.POST['section']
        num_sections = request.POST['num_sections']
        oh = request.POST['office_hours']
        ta = request.POST['TAs']
        meet = request.POST['meet']
        disc = request.POST['disc']
        meet_val = True
        disc_val = False
        semester = Semester.objects.filter(open=True).first()
        if meet == 'yes':
            meet_val = True
        if disc == 'yes':
            disc_val = True

        c = Course(assigned_to_email = request.user.username, time_text=time, course_title=title, description_text=description,
                   professor_text=professor_name, email_text=professor_email, pub_date=datetime.now(), course_id=id, has_meetings=meet_val,
                   has_discussion=disc_val, section=section, num_sections=num_sections, num_office_hours=oh, num_tas=ta, semester=semester)
        c.save()
        send_mail(
            'Successfully Created Course',
            title,
            settings.EMAIL_HOST_USER,
            ['zhongpd@bc.edu'],
            fail_silently=True,
        )
        return redirect('/view_apps/')
    else:
        context={"course_names": COURSE_NAMES, "course_ids": COURSE_IDS, "course_times": COURSE_TIMES}
        return render(request, 'view_apps/create_course.html', context)

def create_semester(request):
    if request.method == "POST":
        form = SemesterForm(request.POST)
        if form.is_valid():
            sem = form.save()
            return redirect('/admin/')
    else:
        form = SemesterForm()
    return render(request, 'view_apps/create_semester.html', {
        'form':form
    })


def delete_course(request, id):
    Course.objects.all().filter(course_id=id).delete()
    send_mail(
        'Successfully Deleted Course',
        "Succesfully deleted course with ID " + id,
        settings.EMAIL_HOST_USER,
        ['sheppaga@bc.edu'],
        fail_silently=True,
    )
    return redirect('/view_apps/')



def apply(request, id):
    MAX_APPLICATIONS = 5
    if request.method == "POST":
        user=request.user
        student_profile = Stud_profile.objects.get(user=user)
        student_email = student_profile.email
        student_name = f"{student_profile.first_name} {student_profile.last_name}"
        if App.objects.filter(user=user).exists():
            c = App.objects.filter(user=user).count()
            num_uses = c + 1
            course_id = id
            office_hours = request.POST['office_hours']
            why_ta = request.POST['why_ta']
            if num_uses > MAX_APPLICATIONS: return render(request, 'view_apps/too_many_apps.html')
            else:
                #IMPORTANT: Assuming course_id is unique
                a = random.randint(10000000, 99999999)
                c = App(user=user, student_text=student_name, email_text=student_email, num_uses = num_uses, office_hours=office_hours, why_ta=why_ta, id = str(a))
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
            a = random.randint(10000000, 99999999)
            c = App(user=user, student_text=student_name, email_text=student_email, office_hours=office_hours, why_ta=why_ta, num_uses=num_uses, id = str(a))
            # IMPORTANT: Assuming course_id is unique
            current_apps = Course.objects.get(course_id=course_id).applications
            current_apps += " " + c.id
            Course.objects.filter(course_id=course_id).update(applications=current_apps)
            c.save()
        return redirect('/view_apps/')
    context={"id": id, "name": "", "email": ""}
    return render(request, 'view_apps/apply.html', context)

#Function added by Aidan
def logoff(request):
    logout(request)
    return redirect('login')

def open_close(request, id):
    Semester.objects.get(name=id).open = Semester.objects.get(name=id).open
    send_mail(
        'Successfully Changed Semester Status',
        "Succesfully Changed Semester with ID " + id,
        settings.EMAIL_HOST_USER,
        ['sheppaga@bc.edu'],
        fail_silently=True,
    )
    return redirect('/view_apps/')

def delete_semester(request, id):
    Semester.objects.all().filter(name=id).delete()
    send_mail(
        'Successfully Deleted Semester',
        "Succesfully deleted Semester with ID " + id,
        settings.EMAIL_HOST_USER,
        ['sheppaga@bc.edu'],
        fail_silently=True,
    )
    return redirect('/view_apps/')