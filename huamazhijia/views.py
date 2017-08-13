from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def passin(request):
    context = {}
    return render(request, 'index.html', context)
