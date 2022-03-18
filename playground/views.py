from django.http import HttpResponse
from django.shortcuts import render

def say_hello():
    return HttpResponse("Hello, World!")