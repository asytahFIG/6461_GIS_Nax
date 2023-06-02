from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Mont Noble welcome page")

# Create your views here.
