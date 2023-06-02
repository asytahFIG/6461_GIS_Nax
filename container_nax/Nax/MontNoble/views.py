from django.http import HttpResponse
from .models import Forest

def index(request):
    forests=Forest.objects.filter(type="forest")
    return HttpResponse(forests[0].name)

# Create your views here.
