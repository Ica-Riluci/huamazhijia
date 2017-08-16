from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

def passin(request):
    context = {
        'warninfo' : '',
    }
    if (request.COOKIES.get('userexists', 'true') == 'false'):
        context['warninfo'] = '[登录失败]用户不存在'
        response = render(request, 'entry/index.html', context)
        response.set_cookie(key='userexists', value='true', max_age=None)
    elif (request.COOKIES.get('passwordcorrect', 'true') == 'false'):
        context['warninfo'] = '[登录失败]密码不正确'
        response = render(request, 'entry/index.html', context)
        response.set_cookie(key='passwordcorrect', value='true', max_age=None)
    elif (request.COOKIES.get('usernameempty', 'false') == 'true'):
        context['warninfo'] = '[登录失败]用户名为空'
        response = render(request, 'entry/index.html', context)
        response.set_cookie(key='usernameempty', value='false', max_age=None)
    elif (request.COOKIES.get('passwordempty', 'false') == 'true'):
        context['warninfo'] = '[登录失败]密码为空'
        response = render(request, 'entry/index.html', context)
        response.set_cookie(key='passwordempty', value='false', max_age=None)
    else:
        response = render(request, 'entry/index.html', context)
    return response

def studentsignup(request):
    context = {
        'unwarn' : '',
        'pwwarn' : '',
    }
    _repeat = request.COOKIES.get('userrepeat', 'false')
    _diff = request.COOKIES.get('passworddiff', 'false')
    if (_repeat == 'true'):
        context['unwarn'] = '该用户名已存在'
        response = render(request, 'entry/signup.html', context)
        response.set_cookie(key='userrepeat', value='false')
    elif (_diff == 'true'):
        context['pwwarn'] = '两次密码不一致'
        response = render(request, 'entry/signup.html', context)
        response.set_cookie(key='passworddiff', value='false')
    else:
        response = render(request, 'entry/signup.html', context)
    return response
