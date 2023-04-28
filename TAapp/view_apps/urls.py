from django.urls import path

from . import views

app_name = 'view_apps'
urlpatterns = [
    path('', views.index, name='index'),
    path('student', views.index, name='student'),
    path('professor', views.index, name='professor'),
    path('create_course', views.create_course, name='create_course'),
    path('apply/<str:id>/', views.apply, name='apply'),
    path('applications/<str:id>/', views.applications, name='applications'),
    path('applications/<str:id>/<str:name>', views.assign_student, name='assign_student'),
    path('logoff', views.logoff, name='logoff'),

]
