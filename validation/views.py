from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.urls import reverse

from .models import Student

def updatestatus(isonline):
    feedback = HttpResponseRedirect(reverse('validation:studentonlinecheck', args=('1', 'root')))
    if (isonline):
        feedback.set_cookie('online', 'true', 600, None, '/', None, None, False)
    else:
        feedback.set_cookie('online', 'false', None, None, '/', None, None, False)
    return feedback

def studentonlinecheck(request, sourceid, source):
    if (sourceid == '1'):
        _cookie = request.COOKIES.get('online', 'false')
        if (_cookie == 'false'):
            response = HttpResponseRedirect(reverse('entry:passin', args=()))
            response.set_cookie('userexists', 'true', None, None, '/', None, None, False)
            response.set_cookie('passwordcorrect', 'true', None, None, '/', None, None, False)
            response.set_cookie('usernameempty', 'false', None, None, '/', None, None, False)
            response.set_cookie('passwordempty', 'false', None, None, '/', None, None, False)
        else:
            response = HttpResponseRedirect(reverse('studentinterface:index',args=()))
    return response

def studentlogin(request):
    if (request.method == 'POST'):
        _username = request.POST['username']
        _password = request.POST['password']
        if (_username == ''):
            response = HttpResponseRedirect(reverse('entry:passin', args=()))
            response.set_cookie('usernameempty', 'true', None, None, '/', None, None, False)
            return response
        if (_password == ''):
            response = HttpResponseRedirect(reverse('entry:passin', args=()))
            response.set_cookie('passwordempty', 'true', None, None, '/', None, None, False)
            return response
        try:
            user = Student.objects.get(username=_username)
            if (user.password != _password):
                response = HttpResponseRedirect(reverse('entry:passin', args=()))
                response.set_cookie('passwordcorrect', 'false', None, None, '/', None, None, False)
                print('here')
                return response
            updatestatus(True)
            return HttpResponseRedirect(reverse('studentinterface:index', args=()))
        except:
            response = HttpResponseRedirect(reverse('entry:passin', args=()))
            response.set_cookie('userexists', 'false', None, None, '/', None, None, False)
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
            response.set_cookie('userrepeat', 'true', None, None, '/', None, None, False)
            return response
        except:
            if (_password != pwconfirm):
                response = HttpResponseRedirect(reverse('entry:studentsignup', args=()))
                response.set_cookie('passworddiff', 'true', None, None, '/', None, None, False)
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
