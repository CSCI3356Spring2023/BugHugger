from django.contrib import admin

from .models import Prof_profile, Stud_profile

admin.site.site_url = "/view_apps/admin"

admin.site.register(Prof_profile)
admin.site.register(Stud_profile)