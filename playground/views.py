from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def say_hello(request):
    return HttpResponse("Hello, Wolrd!")


def say_hello_html(request):
    return render(request, 'playground/hello.html', {'name': '나혀니'})

def say_bye(request):
    return render(request, 'playground/bye.html')