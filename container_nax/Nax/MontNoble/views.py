from django.http import HttpResponse
from .models import Forest, Ski_slope, Hotel, Hut, Facilities, Summit, Chair_lift, Parking, Restaurant, Transportation
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from django.core.serializers import serialize
from shapely.geometry import Polygon

from MontNoble.geometry_manager import load_shapely_from_geodjango

import shapely.wkt

def index(request):
    return render (request, 'MontNoble/index.html')

# Home page with map
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
    hotels=Hotel.objects.filter(cost="$$")
    return HttpResponse(hotels[0].geom)

def summit(request):
    summits=Summit.objects.order_by('-name')
    return HttpResponse(summits[0].geom)

# Serialized objects to show on map - polygons
def forestsjson(request):
    forests=Forest.objects.all()
    ser=serialize('geojson', forests, geometry_field='geom', fields=('name', ))
    return HttpResponse(ser, content_type='json')

def skiSlopesjson(request):
    skiSlopes=Ski_slope.objects.all()
    ser=serialize('geojson', skiSlopes, geometry_field='geom', fields=('name', 'difficulty'))
    return HttpResponse(ser, content_type='json')

def facilitiesjson(request):
    facilities=Facilities.objects.all()
    ser=serialize('geojson', facilities, geometry_field='geom', fields=('name', ))
    return HttpResponse(ser, content_type='json')

def hotelsjson(request):
    hotels=Hotel.objects.all()
    ser=serialize('geojson', hotels, geometry_field='geom', fields=('name', ))
    return HttpResponse(ser, content_type='json')

def restaurantsjson(request):
    restaurants=Restaurant.objects.all()
    ser=serialize('geojson', restaurants, geometry_field='geom', fields=('name', ))
    return HttpResponse(ser, content_type='json')

def parkingsjson(request):
    parkings=Parking.objects.all()
    ser=serialize('geojson', parkings, geometry_field='geom', fields=('name', ))
    return HttpResponse(ser, content_type='json')

def hutsjson(request):
    huts=Hut.objects.all()
    ser=serialize('geojson', huts, geometry_field='geom', fields=('name', ))
    return HttpResponse(ser, content_type='json')


# Serialized objects to show on map - points

def summitsjson(request):
    summits=Summit.objects.all()
    ser=serialize('geojson', summits, geometry_field='geom', fields=('name', ))
    return HttpResponse(ser, content_type='json')

def transportationjson(request):
    transportation=Transportation.objects.all()
    ser=serialize('geojson', transportation, geometry_field='geom', fields=('name', ))
    return HttpResponse(ser, content_type='json')

# Serilized objects to show on map - lines
def chairLiftsjson(request):
    chairLifts=Chair_lift.objects.all()
    ser=serialize('geojson', chairLifts, geometry_field='geom', fields=('name', ))
    return HttpResponse(ser, content_type='json')


