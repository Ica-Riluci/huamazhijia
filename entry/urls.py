from django.conf.urls import url

from . import views

app_name = 'entry'

urlpatterns = [
    url(r'^$', views.passin, name='passin'),
    url(r'^sign-up/$', views.studentsignup, name='studentsignup'),
]
