from django.contrib.gis.db import models

# Create your models here.
# Ski resort
class Ski_slope(models.Model):
    id = models.IntegerField
    geom = models.MultiPolygonField(srid=4326,null=True) 
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    obj_type = models.CharField(max_length=100)
    difficulty = models.IntegerField()
    class Meta:
       db_table = "Ski_slope"

class Chair_lift(models.Model):
    id = models.IntegerField
    geom = models.MultiLineStringField(srid=4326,null=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    obj_type = models.CharField(max_length=100)
    class Meta:
        db_table = "Chair_lift"

# Transport
class Transportation(models.Model):
    id = models.IntegerField
    geom = models.PointField(srid=4326,null=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    obj_type = models.CharField(max_length=100)
    dest = models.CharField(max_length=100)
    available = models.IntegerField(max_length=1)
    altitude =  models.IntegerField(max_length=6)
    subtype = models.CharField(max_length=100)
    class Meta:
        db_table = "Transportation"

class Parking(models.Model):
    id = models.IntegerField
    geom = models.MultiPolygonField(srid=4326,null=True) 
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    obj_type = models.CharField(max_length=100)
    capacity = models.IntegerField(max_length=6)
    available = models.IntegerField(max_length=1)
    class Meta:
        db_table = "Parking"

# Building
class Restaurant(models.Model):
    id = models.IntegerField
    geom = models.MultiPolygonField(srid=4326,null=True) 
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    obj_type = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    available = models.IntegerField(max_length=1)
    class Meta:
        db_table = "Restaurant"

class Hotel(models.Model):
    id = models.IntegerField
    geom = models.MultiPolygonField(srid=4326,null=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    obj_type = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    available = models.IntegerField(max_length=1)
    nb_beds = models.IntegerField(max_length=6)
    class Meta:
        db_table = "Hotel"

class Hut(models.Model):
    id = models.IntegerField
    geom = models.MultiPolygonField(srid=4326,null=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    obj_type = models.CharField(max_length=100)
    altitude = models.IntegerField(max_length=6)
    available = models.IntegerField(max_length=1)
    nb_beds = models.IntegerField(max_length=6)
    class Meta:
        db_table = "Hut"

class Facilities(models.Model):
    id = models.IntegerField
    geom = models.MultiPolygonField(srid=4326,null=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    obj_type = models.CharField(max_length=100)
    function = models.CharField(max_length=100)
    available = models.IntegerField()
    class Meta:
        db_table = "Facilities"

# Nature
class Forest(models.Model):
    id = models.IntegerField
    geom = models.MultiPolygonField(srid=4326,null=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    obj_type = models.CharField(max_length=100)
    protected = models.IntegerField(max_length=1)
    class Meta:
        db_table = "Forest"


class Summit(models.Model):
    id = models.IntegerField
    geom = models.PointField(srid=4326,null=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    obj_type = models.CharField(max_length=100)
    altitude =  models.IntegerField(max_length=6)
    class Meta:
        db_table = "Summit"














