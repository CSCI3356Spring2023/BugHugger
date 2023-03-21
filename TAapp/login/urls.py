from django.urls import path

from . import views

app_name = 'login'
urlpatterns = [
    path('', views.login_user, name='login'),
    path('login/create_student', views.user_create_student, name='create_student'),
    path('login/create_professor', views.user_create_professor, name='create_professor'),
]