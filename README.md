# Projet-2-Q2

## Installer l'application en local
##### 1. Créez d'abord un mini environement et activez le. 

Pour rappel, vous pouvez retrouver les étapes ici : http://renaud-detry.net/teaching/flask/installation.html

##### 2. Une fois le mini environement activé, clonez le dépôt GitHub.

>git clone https://github.com/Martimini/Projet-2-Q2.git

##### 3. Installez les packages nécessaires au fonctionnement du site. 

>pip install -r requirements.txt



## Pour lancer le site en local

>set FLASK_APP=flaskr

>flask run 

Vous obiendrez un lien à copier/coller directement dans la barre de navigation du moteur de recherche

## Structure du dépôt

### Le dossier flaskr

Le dossier flaskr regroupe tous les fichiers liés au fonctionnement de l'application. 

A savoir :
1. Les templates & les fichiers statiques
2. __init__.py
3. Base_de_donnée_sql.sql & db.py
4. show_graph.py

#### 1. Les templates & les fichiers statiques

Les templates sont tous les fichiers Html nécessaires à l'application tandis que les fichiers statiques sont les fichiers CSS relié au Html.

- accueil.html et styleacceuil.css représentent la page principale
- graph.html et stylegraph.css correspondent à la mise en page des graphes affichés 

#### 2. __init__.py

C'est "l'usine à application". C'est dans ce fichier python que tout est regroupé.

#### 3. db.py & Base_de_donnée_sql.sql

db.py s'occupe de lier la base de donnée Base_de_donnée_sql.sql à l'application.

#### 4. show_graph.py 

C'est le fichier qui s'occupe de montrer les graphes correspondant aux résultats des formulaires reçus via accueil.html. Il renvoie ces graphes en renvoyant vers graph.html

### setup.py, MANIFEST.in & requirements.txt

Ce sont les fichiers nécessaires au téléchargement de l'application.

## Les contribueurs
Groupe P2_Vincent_5 :
- Martin Melen
- Vincent Wuillaume
- Noah Fraiture
- Lyse Grolaux
