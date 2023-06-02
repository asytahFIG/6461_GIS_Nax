from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, friend. There you'll find Switzerland.")

# Create your views here.
