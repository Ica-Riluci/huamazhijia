from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.urls import reverse

from .models import Student

def studentlogin(request):
    if (request.method == 'POST'):
        _username = request.POST['username']
        _password = request.POST['password']
        if (_username == ''):
            settings.USER_NULL = True
            return HttpResponseRedirect(reverse('entry:passin', args=()))
        if (_password == ''):
            settings.PW_NULL = True
            return HttpResponseRedirect(reverse('entry:passin', args=()))
        try:
            user = Student.objects.get(username=_username)
            if (user.password != _password):
                settings.PW_NOT_CORRECT = True
                return HttpResponseRedirect(reverse('entry:passin', args=()))
            return HttpResponse('studentlogin')
        except:
            settings.USER_NOT_EXIST = True
            return HttpResponseRedirect(reverse('entry:passin', args=()))
    else:
        return HttpResponseRedirect(reverse('entry:passin', args=()))

def studentsignup(request):
    if (request.method == 'POST'):
        _username = request.POST['username']
        _password = request.POST['password']
        pwconfirm = request.POST['passwordc']
        try:
            user = Student.objects.get(username=_username)
            settings.USER_REPEAT = True
            return HttpResponseRedirect(reverse('entry:studentsignup', args=()))
        except:
            if (_password != pwconfirm):
                settings.PW_CON_FAIL = True
                return HttpResposneRedirect(reverse('entry:studentsignup', args=()))
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
