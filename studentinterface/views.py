from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    context = {}
    return  render(request, 'studentinterface/index.html', context)
