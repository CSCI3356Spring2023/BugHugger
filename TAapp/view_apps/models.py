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

    def __str__(self):
        return self.course_id


