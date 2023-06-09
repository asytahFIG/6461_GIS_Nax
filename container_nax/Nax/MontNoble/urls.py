from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('skiDomain/', views.skiDomain, name='skiDomain'),
    path('forests.json', views.forestsjson, name='forestsjson'),
    path('skiSlopes.json', views.skiSlopejson, name='skiSlopejson'),
    path('hotel', views.hotel, name='hotel'),
    path('slopesForests', views.slopesForests, name='slopesForests'),
    path('slopeForests/<int:slope_id>', views.slopeForests, name='slopeForests'),
]
