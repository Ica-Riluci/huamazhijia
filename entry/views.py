from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

def passin(request):
    context = {
        'warninfo' : '',
    }
    if (settings.USER_NOT_EXIST):
        context['warninfo'] = '[登录失败]用户不存在'
        settings.USER_NOT_EXIST = False
    if (settings.PW_NOT_CORRECT):
        context['warninfo'] = '[登录失败]密码不正确'
        settings.PW_NOT_CORRECT = False
    if (settings.USER_NULL):
        context['warninfo'] = '[登录失败]用户名为空'
        settings.USER_NULL = False
    if (settings.PW_NULL):
        context['warninfo'] = '[登录失败]密码为空'
        settings.PW_NULL = False
    return render(request, 'entry/index.html', context)

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
