import uuid
from django.db import models
from django.contrib.auth.models import User
import random

class Semester(models.Model):
    name = models.CharField(max_length=12, primary_key=True)
    start = models.DateField()
    end = models.DateField()
    open = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name

class Course(models.Model):
    course_title = models.CharField(max_length=100)
    description_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    professor_text = models.CharField(max_length=50)
    email_text = models.CharField(max_length=50, blank=True)
    course_id = models.CharField(max_length=15)
    time_text = models.CharField(max_length=15)
    has_meetings = models.BooleanField()
    has_discussion = models.BooleanField()
    section = models.IntegerField()
    num_sections = models.IntegerField()
    num_office_hours = models.IntegerField()
    num_tas = models.IntegerField()
    assigned_to_email = models.CharField(max_length=100)
    applications = models.CharField(max_length=1000, default="", blank = True)
    assigned_students = models.CharField(max_length=1000, default="", blank = True)
    accepted_students = models.CharField(max_length=1000, default="", blank = True)
    num_assigned = models.IntegerField(default = 0, blank = True)
    num_accepted = models.IntegerField(default = 0, blank = True)
    is_open = models.BooleanField(default = True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.course_id
    
class App(models.Model):
    a = random.randint(10000000, 99999999)
    is_visible = models.BooleanField(default = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    student_text = models.CharField(max_length=50, blank=True)
    email_text = models.CharField(max_length=50, blank=True)
    office_hours = models.CharField(max_length=15, blank=True)
    why_ta = models.CharField(max_length=500, blank=True)
    num_uses = models.IntegerField(default=0)
    id = models.CharField(max_length=1000, primary_key=True, default=str(a), )
    # TODO: file
    # models.FileField(upload_to='PLACE_HERE')

    def __str__(self):
        return self.user.username





