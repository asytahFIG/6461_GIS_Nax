from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('skiDomain/', views.skiDomain, name='skiDomain'),
    path('forests.json', views.forestsjson, name='forestsjson'),
    path('hotel', views.hotel, name='hotel'),
    path('slopesForests', views.slopesForests, name='slopesForests'),
    path('slopeForests/<int:slope_id>', views.slopeForests, name='slopeForests'),
    path('skiSlopes.json', views.skiSlopesjson, name='skiSlopesjson'),
    path('facilities.json', views.facilitiesjson, name='facilitiesjson'),
    path('hotels.json', views.hotelsjson, name='hotelsjson'),
    path('restaurants.json', views.restaurantsjson, name='restaurantsjson'),
    path('parkings.json', views.parkingsjson, name='parkingsjson'),
    path('huts.json', views.hutsjson, name='hutsjson'),
    path('hotel', views.hotel, name='hotel'),
]
