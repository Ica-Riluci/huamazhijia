from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.urls import reverse

from .models import Student

def studentonlinecheck(request, source):
    if (source == '1'):
        _cookie = request.COOKIES.get('online', None)
        if (_cookie == None):
            response = HttpResponseRedirect(reverse('entry:passin', args=()))
            response.set_cookie(key='online', value='true', max_age=600)
            response.set_cookie(key='userexists', value='true', max_age=None)
            response.set_cookie(key='passwordcorrect', value='true', max_age=None)
            response.set_cookie(key='usernameempty', value='false', max_age=None)
            response.set_cookie(key='passwordempty', value='false', max_age=None)
        else:
            response = HttpResponseRedirect(reverse('studentinterface:index',args=()))
    return response

def studentlogin(request):
    if (request.method == 'POST'):
        _username = request.POST['username']
        _password = request.POST['password']
        if (_username == ''):
            response = HttpResponseRedirect(reverse('entry:passin', args=()))
            response.set_cookie(key='usernameempty', value='true')
            return response
        if (_password == ''):
            response = HttpResponseRedirect(reverse('entry:passin', args=()))
            response.set_cookie(key='passwordempty', value='true')
            return response
        try:
            user = Student.objects.get(username=_username)
            if (user.password != _password):
                response = HttpResponseRedirect(reverse('entry:passin', args=()))
                response.set_cookie(key='passwordcorrect', value='false')
                return response
            feedback = HttpResponseRedirect(reverse('validation:studentonlinecheck', args=('1')))
            feedback.set_cookie(key='online', value='true', max_age=600)
            return HttpResponseRedirect(reverse('studentinterface:index', args=()))
        except:
            response = HttpResponseRedirect(reverse('entry:passin', args=()))
            response.set_cookie(key='userexists', value='false')
            return response
    else:
        return HttpResponseRedirect(reverse('entry:passin', args=()))

def studentsignup(request):
    if (request.method == 'POST'):
        _username = request.POST['username']
        _password = request.POST['password']
        pwconfirm = request.POST['passwordc']
        try:
            user = Student.objects.get(username=_username)
            response = HttpResponseRedirect(reverse('entry:studentsignup', args=()))
            response.set_cookie(key='userrepeat', value='true')
            return response
        except:
            if (_password != pwconfirm):
                response = HttpResponseRedirect(reverse('entry:studentsignup', args=()))
                response.set_cookie(key='passworddiff', value='true')
                return response
            _email = request.POST['email']
            _name = request.POST['name']
            _school = request.POST['school']
            _grade = int(request.POST['grade'])
            _class = request.POST['class']
            _sphone = request.POST['sphone']
            _pphone = request.POST['pphone']
            newstudent = Student(username=_username, password=_password, name=_name,
            sphone=_sphone, pphone=_pphone, school=_school, emailadd=_email, classx=_class,
            grade=_grade, gender=2, potrait=None)
            newstudent.save()
            return HttpResponseRedirect(reverse('entry:passin', args=()))
