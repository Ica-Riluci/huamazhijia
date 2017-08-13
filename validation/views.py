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
            return HttpResponse('studentlogin')
        except:
            settings.USER_NOT_EXIST = True
            return HttpResponseRedirect(reverse('entry:passin', args=()))
