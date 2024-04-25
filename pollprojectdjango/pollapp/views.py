from django.shortcuts import render

# Create your views here.


class Httpresponse:
    pass


def welcome(request):
    return Httpresponse("Welcome to PollApp")
