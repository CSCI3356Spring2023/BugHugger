from django.shortcuts import render

from .models import Course


def index(request):
    latest_course_list = Course.objects.order_by('-pub_date')[:5]
    context = {'latest_course_list': latest_course_list}
    return render(request, 'view_apps/index.html', context)

