from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome(request):
    return HttpResponse("welcome to poll app")