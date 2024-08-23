from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_modblog (response):
    return HttpResponse("Hello, Modders!")
