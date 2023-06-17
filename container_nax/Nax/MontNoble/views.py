from django.http import Http404, HttpResponse, HttpResponseNotFound
from .models import Forest, Ski_slope, Hotel, Hut, Facilities, Summit, Chair_lift, Parking, Restaurant, Transportation
from django.template import loader
from django.shortcuts import render
from django.core.serializers import serialize
from shapely.geometry import Polygon
from django.core.serializers import serialize

from MontNoble.geometry_manager import load_shapely_from_geodjango, get_list_of_neighbors_polygon, get_list_of_neighbors_line

def index(request):
    return render (request, 'MontNoble/index.html')

# Home page with map
def skiDomain(request):
    context = {}
    return render(request, 'MontNoble/skiDomain.html', context)

# Create your views here.

# Services
def chooseDifficulty(request):
    return render(request, "MontNoble/chooseDifficulty.html")

def domainByDifficulty(request, difficulty):
    ski_slopes=Ski_slope.objects.order_by('-name')

    if (difficulty == 1):
        ski_slopes = [s for s in ski_slopes if (s.difficulty <= 2)]
    elif (difficulty == 2):
        ski_slopes = [s for s in ski_slopes if (s.difficulty <= 4)]

    neighborHotels, neighborRestaurants,  neighborHuts = [], [], []

    for ski_slope in ski_slopes:
        # Get neigbor services
        neighborHotels.extend(get_list_of_neighbors_polygon(ski_slope, Hotel.objects.order_by('-name')))
        neighborRestaurants.extend(get_list_of_neighbors_polygon(ski_slope, Restaurant.objects.order_by('-name')))
        neighborHuts.extend(get_list_of_neighbors_polygon(ski_slope, Hut.objects.order_by('-name')))

    # Serialize
    slope_ser=serialize('geojson',ski_slopes,geometry_field='geom')
    hotels_ser=serialize('geojson',neighborHotels,geometry_field='geom')
    restaurants_ser=serialize('geojson',neighborRestaurants,geometry_field='geom')
    huts_ser=serialize('geojson',neighborHuts,geometry_field='geom')
    chair_lift_ser = serialize('geojson',Chair_lift.objects.all() ,geometry_field='geom')

    context = {'skiSlopes': slope_ser, 'hotels': hotels_ser, 'restaurants': restaurants_ser, 'huts': huts_ser,
               'chairLifts': chair_lift_ser}
    return render(request, "MontNoble/domainByDifficulty.html", context)


def slopesServices(request):
    return render(request, "MontNoble/slopesServices.html")

def slopeServices(request, slope_id):
    try:
        ski_slope=Ski_slope.objects.get(pk=slope_id)
    except Ski_slope.DoesNotExist:
        raise Http404("Slope not found!!")
    
    # Get neigbor services
    neighborHotels=get_list_of_neighbors_polygon(ski_slope, Hotel.objects.order_by('-name'))
    neighborRestaurants=get_list_of_neighbors_polygon(ski_slope, Restaurant.objects.order_by('-name'))
    neighborHuts=get_list_of_neighbors_polygon(ski_slope, Hut.objects.order_by('-name'))
    
    # Serialize
    ski_slope_arr = [ski_slope]
    slope_ser=serialize('geojson',ski_slope_arr,geometry_field='geom')
    hotels_ser=serialize('geojson',neighborHotels,geometry_field='geom')
    restaurants_ser=serialize('geojson',neighborRestaurants,geometry_field='geom')
    huts_ser=serialize('geojson',neighborHuts,geometry_field='geom')

    context = {'skiSlope': slope_ser, 'hotels': hotels_ser, 'restaurants': restaurants_ser, 'huts': huts_ser}
    return render(request, "MontNoble/slopeServices.html", context)

def slopesForests(request):
    return render(request, 'MontNoble/slopesForests.html')

def slopeForests(request, slope_id):
    try:
        ski_slope=Ski_slope.objects.get(pk=slope_id)
    except Ski_slope.DoesNotExist:
        raise Http404("Slope not found!!")

    all_forests=Forest.objects.order_by('-name')
    neighborForests = get_list_of_neighbors_polygon(model=ski_slope, others_list=all_forests)

    for_ser=serialize('geojson',neighborForests,geometry_field='geom',fields=("name", ))
    ski_slope_arr = [ski_slope]
    ser=serialize('geojson',ski_slope_arr,geometry_field='geom',fields=("name", ))

    return render(request,'MontNoble/slopeForests.html', {'neighborForests': for_ser, 'skiSlope': ser})

def chairLiftForests(request, chairLift_id):
    try:
        chair_lift=Chair_lift.objects.get(pk=chairLift_id)
    except Ski_slope.DoesNotExist:
        raise Http404("Slope not found!!")

    all_forests=Forest.objects.order_by('-name')
    neighborForests = get_list_of_neighbors_line(model=chair_lift, others_list=all_forests)

    for_ser=serialize('geojson',neighborForests,geometry_field='geom',fields=("name", ))
    ser=serialize('geojson',[chair_lift],geometry_field='geom',fields=("name", ))

    return render(request,'MontNoble/chairLiftForests.html', {'neighborForests': for_ser, 'chairLift': ser})

# Views for services
def hotel(request):
    hotels=Hotel.objects.filter(cost="$$")
    return HttpResponse(hotels[0].geom)

def summit(request):
    summits=Summit.objects.order_by('-name')
    return HttpResponse(summits[0].geom)

# Serialized objects to show on map - polygons
def forestsjson(request):
    forests=Forest.objects.all()
    ser=serialize('geojson', forests, geometry_field='geom')
    return HttpResponse(ser, content_type='json')

def skiSlopesjson(request):
    skiSlopes=Ski_slope.objects.all()
    ser=serialize('geojson', skiSlopes, geometry_field='geom')
    return HttpResponse(ser, content_type='json')

def facilitiesjson(request):
    facilities=Facilities.objects.all()
    ser=serialize('geojson', facilities, geometry_field='geom')
    return HttpResponse(ser, content_type='json')

def hotelsjson(request):
    hotels=Hotel.objects.all()
    ser=serialize('geojson', hotels, geometry_field='geom')
    return HttpResponse(ser, content_type='json')

def restaurantsjson(request):
    restaurants=Restaurant.objects.all()
    ser=serialize('geojson', restaurants, geometry_field='geom')
    return HttpResponse(ser, content_type='json')

def parkingsjson(request):
    parkings=Parking.objects.all()
    ser=serialize('geojson', parkings, geometry_field='geom')
    return HttpResponse(ser, content_type='json')

def hutsjson(request):
    huts=Hut.objects.all()
    ser=serialize('geojson', huts, geometry_field='geom')
    return HttpResponse(ser, content_type='json')


# Serialized objects to show on map - points
def summitsjson(request):
    summits=Summit.objects.all()
    ser=serialize('geojson', summits, geometry_field='geom')
    return HttpResponse(ser, content_type='json')

def transportationjson(request):
    transportation=Transportation.objects.all()
    ser=serialize('geojson', transportation, geometry_field='geom')
    return HttpResponse(ser, content_type='json')

# Serilized objects to show on map - lines
def chairLiftsjson(request):
    chairLifts=Chair_lift.objects.all()
    ser=serialize('geojson', chairLifts, geometry_field='geom')
    return HttpResponse(ser, content_type='json')


