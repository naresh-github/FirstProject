from django.shortcuts import render
from django.http import HttpResponse
def saywelcome(request):
    return HttpResponse("<h1> welcome To Django</h1>")


# Create your views here.
