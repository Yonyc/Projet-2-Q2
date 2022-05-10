# Projet-2-Q2

## Installer l'application en local
##### 1. Rentrez dans le dossier du projet "Projet-2-Q2-main" à l'aide la commande "cd". 

>cd\
>
Pour revenir à la racine de l'ordinateur suivit de 

> cd %Chemin du dossier projet%

Pour arriver au dossier du projet

##### 2. Créer l'environnement virtuel

Pour cela on suit les instructions du site du cours. Si vous êtes sur un autre os que windows il suffit de suivre les instructions du site http://renaud-detry.net/teaching/flask/installation.html. Nous rappelons ici les instructions pour windows :
> py -3 -m venv venv (pour créer l'environnement)
> venv\Scripts\activate (pour l'activer)

##### 3. Installez les packages nécessaires au fonctionnement du site. 

>pip install -r requirements.txt

##### 4. Initialiser la base de donnée

>python flaskr/Base_de_donnee/Base.py

##### 5. Pour lancer le site en local

###### Pour Windows :

>set FLASK_APP=flaskr

>flask run 

###### Pour Linux et Mac :

$ export FLASK_APP=flaksr

$ flask run

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


database.py est le fichier qui crée la structure des tables de la base de donnée
basa_de_donnée_sql.db est la base de donnée en question
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
