from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Prof_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60, blank=True)
    department = models.CharField(max_length=60, blank=True)
    email = models.EmailField(max_length=60, blank=True)


class Stud_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60, blank=True)
    email = models.EmailField(max_length=60, blank=True)
    school = models.CharField(max_length=10, blank=True)
    major = models.CharField(max_length=60, blank=True)
    minors = models.CharField(max_length=200, blank=True)
    blurb = models.TextField(max_length=500, blank=True)

@receiver(post_save, sender=User)
def create_prof_profile(sender, instance, created, **kwargs):
    if created:
        Prof_profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_prof_profile(sender, instance, **kwargs):
    instance.prof_profile.save()

    
@receiver(post_save, sender=User)
def create_stud_profile(sender, instance, created, **kwargs):
    if created:
        Stud_profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_stud_profile(sender, instance, **kwargs):
    instance.stud_profile.save()
