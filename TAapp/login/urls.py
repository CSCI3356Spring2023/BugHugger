from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.login_user, name='login'),
    path('login/create', views.user_create, name='create'),
]