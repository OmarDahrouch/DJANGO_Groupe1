from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    # Do something here...
    return HttpResponse("Hello, world!")
