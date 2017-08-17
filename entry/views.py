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
        response.set_cookie('userexists', 'true', None, None, '/', None, None, False)
    elif (request.COOKIES.get('passwordcorrect', 'true') == 'false'):
        context['warninfo'] = '[登录失败]密码不正确'
        response = render(request, 'entry/index.html', context)
        response.set_cookie('passwordcorrect', 'true', None, None, '/', None, None, False)
    elif (request.COOKIES.get('usernameempty', 'false') == 'true'):
        context['warninfo'] = '[登录失败]用户名为空'
        response = render(request, 'entry/index.html', context)
        response.set_cookie('usernameempty', 'false', None, None, '/', None, None, False)
    elif (request.COOKIES.get('passwordempty', 'false') == 'true'):
        context['warninfo'] = '[登录失败]密码为空'
        response = render(request, 'entry/index.html', context)
        response.set_cookie('passwordempty', 'false', None, None, '/', None, None, False)
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
        response.set_cookie('userrepeat', 'false', None, None, '/', None, None, False)
    elif (_diff == 'true'):
        context['pwwarn'] = '两次密码不一致'
        response = render(request, 'entry/signup.html', context)
        response.set_cookie('passworddiff', 'false', None, None, '/', None, None, False)
    else:
        response = render(request, 'entry/signup.html', context)
    return response
