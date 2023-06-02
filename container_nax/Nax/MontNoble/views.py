from django.shortcuts import render
from django.http import HttpResponse
from .models import Forest

def index(request):
    return HttpResponse("hello")


# Create your views here.
