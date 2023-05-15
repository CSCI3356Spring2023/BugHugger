from django.urls import path

from . import views

app_name = 'view_apps'
urlpatterns = [
    path('', views.index, name='index'),
    path('student', views.index, name='student'),
    path('professor', views.index, name='professor'),
    path('admin', views.index, name='admin'),
    path('create_course', views.create_course, name='create_course'),
    path('create_semester', views.create_semester, name='create_semester'),
    path('delete_course/<str:id>/', views.delete_course, name='delete_course'),
    path('delete_semester/<str:id>/', views.delete_semester, name='delete_semester'),
    path('open_close/<str:id>/', views.open_close, name='open_close'),
    path('apply/<str:id>/', views.apply, name='apply'),
    path('applications/<str:id>/', views.applications, name='applications'),
    path('view_courses/<str:sem>/', views.view_courses, name='view_courses'),
    path('applications/<str:id>/<str:name>', views.assign_student, name='assign_student'),
    path('accept/<str:id>/', views.accept, name='accept'),
    path('deny/<str:id>/', views.deny, name='deny'),
    path('logoff', views.logoff, name='logoff'),

]
