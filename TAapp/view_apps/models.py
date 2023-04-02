from django.db import models

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

    def __str__(self):
        return self.course_id
class App(models.Model):
    course_id = models.CharField(max_length=15)
    student_name = models.CharField(max_length=100)
    eagle_id = models.CharField(max_length=15)
    office_hours = models.CharField(max_length=15)
    major = models.CharField(max_length=200)
    why_ta = models.CharField(max_length=500)
    # TODO: file
    # models.FileField(upload_to='PLACE_HERE')

    def __str__(self):
        return self.eagle_id


