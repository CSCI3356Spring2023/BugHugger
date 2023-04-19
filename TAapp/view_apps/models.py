from django.db import models
from django.contrib.auth.models import User
import random

class Course(models.Model):
    course_title = models.CharField(max_length=100)
    description_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    professor_text = models.CharField(max_length=50)
    course_id = models.CharField(max_length=15)
    time_text = models.CharField(max_length=15)
    has_meetings = models.BooleanField()
    has_discussion = models.BooleanField()
    section = models.IntegerField()
    num_sections = models.IntegerField()
    num_office_hours = models.IntegerField()
    num_tas = models.IntegerField()
    assigned_to_email = models.CharField(max_length=100)
    applications = models.CharField(max_length = 1000, default = "")

    def __str__(self):
        return self.course_id
class App(models.Model):
    a = random.randint(10000000, 99999999)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
    office_hours = models.CharField(max_length=15, blank=True)
    why_ta = models.CharField(max_length=500, blank=True)
    num_uses = models.IntegerField(default=0)
    id = models.CharField(max_length = 1000, primary_key=True, default=str(a), )
    # TODO: file
    # models.FileField(upload_to='PLACE_HERE')

    def __str__(self):
        return self.user.username


