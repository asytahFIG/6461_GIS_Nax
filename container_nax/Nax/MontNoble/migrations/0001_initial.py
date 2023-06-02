# Generated by Django 3.2.19 on 2023-06-02 14:49

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chair_lift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('obj_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('obj_type', models.CharField(max_length=100)),
                ('function', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Forest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('obj_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('obj_type', models.CharField(max_length=100)),
                ('cost', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('obj_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('obj_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('obj_type', models.CharField(max_length=100)),
                ('cost', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ski_slope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('obj_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Summit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('obj_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('obj_type', models.CharField(max_length=100)),
                ('dest', models.CharField(max_length=100)),
                ('subtype', models.CharField(max_length=100)),
            ],
        ),
    ]
