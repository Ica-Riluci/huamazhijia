from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse

def passin(request):
    return HttpResponseRedirect(reverse('entry:passin', args=()))
