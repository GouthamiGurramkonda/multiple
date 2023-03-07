from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_function(request):
    return HttpResponse('<h1>This is the first function of app2</h1>')

def second_function(request):
    return HttpResponse('<h1>This is second function of app2</h1>')
