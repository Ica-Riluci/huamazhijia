from django.conf.urls import url

from . import views

app_name = 'validation'

urlpatterns = [
    url(r'^student/login$', views.studentlogin, name='studentlogin'),
    url(r'^student/signup$', views.studentsignup, name='studentsignup'),
]
