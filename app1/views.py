from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_function(request):
    return HttpResponse('<h1><marquee>This is first function of app1</h1></marquee>')

def second_function(request):
    return HttpResponse('<h1><marquee>This is second function of app1</h1></marquee>')
