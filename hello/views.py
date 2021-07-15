from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, World! And everyone out there! This is the Django Version of the App I'm trying to Deploy.")
