from django.contrib import admin

from .models import Course, App, Semester

admin.site.site_url = "/view_apps/admin"
admin.site.register(Course)
admin.site.register(App)
admin.site.register(Semester)