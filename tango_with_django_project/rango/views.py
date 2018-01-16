from django.shortcuts import render

from django.http import HttpResponse

def indec(request):
    return HttpResponse("Rango says hey there partner!")
