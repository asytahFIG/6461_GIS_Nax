from django.http import HttpResponse
from .models import Forest, Ski_slope, Hotel
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from django.core.serializers import serialize
from shapely.geometry import Polygon

from MontNoble.geometry_manager import load_shapely_from_geodjango

import shapely.wkt

def index(request):
    return render (request, 'MontNoble/index.html')

# Create your views here.
def skiDomain(request):
    context = {}
    return render(request, 'MontNoble/skiDomain.html', context)

# Create your views here.
def slopesForests(request):
    ski_slopes=Ski_slope.objects.order_by('-name')
    context = { 'ski_slopes':ski_slopes, }
    return render(request, 'MontNoble/slopesForests.html', context)

def slopeForests(request, slope_id):

    try:
        ski_slope=Ski_slope.objects.get(pk=slope_id)

    except Ski_slope.DoesNotExist:
        raise Http404("City not found!!")

    slope_polygon = load_shapely_from_geodjango(ski_slope)

    all_forests=Forest.objects.order_by('-name')
    neighborForests = []
    for forest in all_forests:
        forest_polygon = load_shapely_from_geodjango(forest)
        if (forest_polygon.intersects(slope_polygon)):
            neighborForests.append(forest)

    return render(request,'MontNoble/slopeForests.html',{'neighborForests': neighborForests})


# Create your views here.
def hotel(request):
    hteols=Hotel.objects.filter(cost="$$")
    return HttpResponse(hteols[0].geom)

def forestsjson(request):
    forests=Forest.objects.all()
    ser=serialize('geojson', forests, geometry_field='geom', fields=('name', ))
    return HttpResponse(ser, content_type='json')

def skiSlopejson(request):
    skiSlopes=Ski_slope.objects.all()
    ser=serialize('geojson', skiSlopes, geometry_field='geom', fields=('name', 'difficulty'))
    return HttpResponse(ser, content_type='json')


