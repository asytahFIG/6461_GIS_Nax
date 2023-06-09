from django.http import HttpResponse
from .models import Forest, Ski_slope, Hotel, Hut, Facilities, Summit, Chair_lift, Parking, Restaurant, Transportation
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from django.core.serializers import serialize

def index(request):
    return render (request, 'MontNoble/index.html')

# Home page with map
def skiDomain(request):
    context = {}
    return render(request, 'MontNoble/skiDomain.html', context)

# Views for services
def hotel(request):
    hotels=Hotel.objects.filter(cost="$$")
    return HttpResponse(hotels[0].name)

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


# Serilized objects to show on map - lines


