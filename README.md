# Projet-2-Q2

## Installer l'application en local
##### 1. Créez d'abord un mini environement et activez le. 

Pour rappel, vous pouvez retrouver les étapes ici : http://renaud-detry.net/teaching/flask/installation.html

##### 2. Une fois le mini environement activé, clonez le dépôt GitHub.

>git clone https://github.com/Martimini/Projet-2-Q2.git

##### 3. Entrez dans le dossier Projet-2-Q2

>cd Projet-2-Q2

##### 4. Installez les packages nécessaires au fonctionnement du site. 

>pip install -r requirements.txt


## Pour lancer le site en local

>set FLASK_APP=flaskr

>flask run 

Vous obiendrez un lien à copier/coller directement dans la barre de navigation du moteur de recherche

## Structure du dépôt

### Les captures d'écran

Captures d'écrans du site et des pages annexes qui affichent les grahes

### Le dossier flaskr

Le dossier flaskr regroupe tous les fichiers liés au fonctionnement de l'application. 

A savoir :
1. Base_de_donnée
2. Tests
3. Les templates & les fichiers statiques
4. __init__.py
5. db.py
6. show_graph.py

#### 1. Base_de_donnée

La base de donnée comme le nom l'indique comprent les données utilisées par le site en l'occurrence dans le cas présent ce sont les informations relatives aux vaches ainsi que les fichiers permettant sa création.

Ce dossier est composé de:
- Un dossier 1002-sql-data qui reprend les fichiers fourni par le tuteur
- Base.py, un fichier permettant la création de la base de donnée
- Héritage_génétique.py, fichier permettant de calculer le pourcentage d'une race d'une vache et de la relier à ses ancêtres
- database.py, fichier montrant la structure de la base de donnée
- Base_de_donnée_sql.sql qui est la base de donnée

#### 2. Tests

Dossiers composé de fichiers tests des fonctions utiles à l'application

#### 3. Les templates & les fichiers statiques

Les templates sont tous les fichiers Html nécessaires à l'application tandis que les fichiers statiques sont les fichiers CSS relié au Html.

- accueil.html et styleacceuil.css représentent la page principale
- graph.html et stylegraph.css correspondent à la mise en page des graphes affichés 

#### 4. __init__.py

C'est "l'usine à application". C'est dans ce fichier python que tout est regroupé.

#### 5. db.py

db.py est un fichier python qui s'occupe de lier la base de donnée Base_de_donnée_sql.sql à l'application (dans __init__.py).

#### 6. show_graph.py 

C'est le fichier qui s'occupe de montrer les graphes correspondant aux résultats des formulaires reçus via accueil.html. Il renvoie ces graphes en renvoyant vers graph.html

### setup.py, MANIFEST.in & requirements.txt

Ce sont les fichiers nécessaires au téléchargement de l'application.

## Les contribueurs
Groupe P2_Vincent_5 :
- Noah Fraiture
- Lyse Grolaux
- Martin Melen
- Vincent Wuillaume
