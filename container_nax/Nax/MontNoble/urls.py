from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.index, name='index'),
    path('skiDomain/', views.skiDomain, name='skiDomain'),

    # Services
    path('slopesServices', views.slopesServices, name='slopesServices'),
    path('slopeServices/<int:slope_id>', views.slopeServices, name='slopeServices'),
    path('slopesForests', views.slopesForests, name='slopesForests'),
    path('slopeForests/<int:slope_id>', views.slopeForests, name='slopeForests'),
    path('chairLiftForests/<int:chairLift_id>', views.chairLiftForests, name='chairLiftForests'),
    path('chooseDifficulty', views.chooseDifficulty, name='chooseDifficulty'),
    path('domainByDifficulty/<int:difficulty>', views.domainByDifficulty, name='domainByDifficulty'),

    # Json to load
    path('forests.json', views.forestsjson, name='forestsjson'),
    path('skiSlopes.json', views.skiSlopesjson, name='skiSlopesjson'),
    path('facilities.json', views.facilitiesjson, name='facilitiesjson'),
    path('hotels.json', views.hotelsjson, name='hotelsjson'),
    path('restaurants.json', views.restaurantsjson, name='restaurantsjson'),
    path('parkings.json', views.parkingsjson, name='parkingsjson'),
    path('huts.json', views.hutsjson, name='hutsjson'),
    path('summits.json', views.summitsjson, name='summitsjson'),
    path('transportation.json', views.transportationjson, name='transportationjson'),
    path('chairLifts.json', views.chairLiftsjson, name='chairLiftsjson'),

    # Tests
    path('hotel', views.hotel, name='hotel'),
    path('summit', views.summit, name='summit'),
    
]
