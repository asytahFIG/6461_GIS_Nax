from django.http import HttpResponse
from .models import Forest, Ski_slope
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from django.core.serializers import serialize

def index(request):
    return render (request, 'MontNoble/index.html')

# Create your views here.
def skiDomain(request):
    context = {}
    return render(request, 'MontNoble/skiDomain.html', context)

def forestsjson(request):
    forests=Forest.objects.all()
    ser=serialize('geojson', forests, geometry_field='geom', fields=('name', ))
    return HttpResponse(ser, content_type='json')

def skiSlopejson(request):
    skiSlopes=Ski_slope.objects.all()
    ser=serialize('geojson', skiSlopes, geometry_field='geom', fields=('name', 'difficulty'))
    return HttpResponse(ser, content_type='json')
