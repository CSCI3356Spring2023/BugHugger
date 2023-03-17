from django.shortcuts import render

from .models import User


def index(request):
    user_list = User.objects
    context = {'user_list': user_list}
    return render(request, 'login/index.html', context)