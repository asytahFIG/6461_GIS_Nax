from django.http import HttpResponse
from .models import Forest

def index(request):
    return HttpResponse("Hello, friend. There you'll find Switzerland.")

# Create your views here.
