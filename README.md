# 646-1 GIS Nax

## Pour installer le projet dans votre environnement local (depuis GitHub)

Commencer par cloner le repository: 

`git clone https://github.com/asytahFIG/6461_GIS_Nax/`

Se rendre dans le dossier "container_nax" où se trouve le docker-compose.yml et exécuter:

`docker-compose up`

Depuis l'interface pgadmin ([localhost](http://localhost:5050/login?next=%2F)) se connecter et ajouter un serveur. Les informations de connection se trouve dans le docker-compose.yml. Une fois la base de donnée démarrée, importer les .shape dans QGIS, puis dans PostGIS.

## Pour installer le projet dans votre environnement local (depuis un zip)

Se rendre dans le dossier "container_nax" où se trouve le docker-compose.yml et exécuter:

`docker-compose up`

La base de donnée étant contenue dans le zip, il n'y pas besoin d'importer les .shp manuellement. 

## Navigation sur le site web

Se rendre à l'adresse localhost sur le port 8000 pour accéder au site.

![image](https://github.com/asytahFIG/6461_GIS_Nax/assets/92582589/14600332-ba13-4b62-b7af-4c4067dc809f)
