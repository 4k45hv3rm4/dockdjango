from django.shortcuts import render
from django.http import HttpResponse


def dock(request):
    return HttpResponse("<h1>Hello World through the eyes of Docker</h1>")
