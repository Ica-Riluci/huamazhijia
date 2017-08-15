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
    if (settings.USER_REPEAT):
        context['unwarn'] = '该用户名已存在'
        settings.USER_REPEAT = False
    elif (settings.PW_CON_FAIL):
        context['pwwarn'] = '两次密码不一致'
        settings.PW_CON_FAIL = False
    return render(request, 'entry/signup.html', context)
