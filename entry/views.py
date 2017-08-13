from django.shortcuts import render
from django.http import HttpResponse

def passin(request):
    context = {}
    return render(request, 'entry/index.html', context)

def studentsignup(request):
    return HttpResponse('studentsignup')
