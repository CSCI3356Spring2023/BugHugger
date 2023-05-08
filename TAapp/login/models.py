from django.db import models
from django.contrib.auth.models import User
import uuid

class Prof_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60, blank=True)
    department = models.CharField(max_length=60, blank=True)
    email = models.EmailField(max_length=60, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True)

class Stud_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60, blank=True)
    email = models.EmailField(max_length=60, blank=True)
    school = models.CharField(max_length=10, blank=True)
    CS_major = models.BooleanField(default=False) #False means minor
    blurb = models.TextField(max_length=500, blank=True)
    year = models.CharField(max_length=40, blank=True)
    currently_hired = models.BooleanField(default=False) #False means open to work
    id = models.UUIDField(default=uuid.uuid4, unique=True)