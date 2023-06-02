from django.contrib.gis.db import models

# Create your models here.

# Ski resort

class Ski_slope(models.Model):
    id = models.IntegerField
    geom=models.MultiPolygonField(srid=4326,null=True) 
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    obj_type = models.CharField(max_length=100)
    difficulty = models.IntegerField

class Chair_lift(models.Model):
    id = models.IntegerField
    geom = models.MultiLineStringField
    geom=models.MultiPolygonField(srid=4326,null=True) 
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    obj_type = models.CharField(max_length=100)

# Transport

class Transportation(models.Model):
    id = models.IntegerField
    geom=models.PointField
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    obj_type = models.CharField(max_length=100)
    dest = models.CharField(max_length=100)
    available = models.IntegerField
    altitude =  models.IntegerField
    subtype = models.CharField(max_length=100)

class Parking(models.Model):
    id = models.IntegerField
    geom=models.MultiPolygonField(srid=4326,null=True) 
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    obj_type = models.CharField(max_length=100)
    capacity = models.IntegerField
    available = models.IntegerField

# Building

class Restaurant(models.Model):
    id = models.IntegerField
    geom=models.MultiPolygonField(srid=4326,null=True) 
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    obj_type = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    available = models.IntegerField

class Hotel(models.Model):
    id = models.IntegerField
    geom=models.MultiPolygonField(srid=4326,null=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    obj_type = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    available = models.IntegerField
    nb_beds = models.IntegerField

class Hut(models.Model):
    id = models.IntegerField
    geom=models.MultiPolygonField(srid=4326,null=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    obj_type = models.CharField(max_length=100)
    altitude = models.IntegerField
    available = models.IntegerField
    nb_beds = models.IntegerField

class Facilities(models.Model):
    id = models.IntegerField
    geom=models.MultiPolygonField(srid=4326,null=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    obj_type = models.CharField(max_length=100)
    function = models.CharField(max_length=100)
    available = models.IntegerField

# Nature

class Forest(models.Model):
    id = models.IntegerField
    geom=models.MultiPolygonField(srid=4326,null=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    obj_type = models.CharField(max_length=100)
    protected = models.IntegerField


class Summit(models.Model):
    id = models.IntegerField
    geom=models.PointField
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    obj_type = models.CharField(max_length=100)
    altitude =  models.IntegerField














