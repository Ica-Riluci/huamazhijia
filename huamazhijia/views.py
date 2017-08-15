from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse

def redirect(request):
    return HttpResponseRedirect(reverse('validation:studentonlinecheck', args=('1')))
