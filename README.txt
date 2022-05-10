Projet 2 - Q2
Guide d'installation de notre site web

Dans l'invite de commande:

1. Rentrez dans le dossier du projet "Projet-2-Q2-main" à l'aide la commande "cd". ("cd\" pour revenir à la racine de l'ordinateur suivit de "cd %chemin du dossier projet%")

2. Créer l'environnement virtuel. Pour cela on suit les instructions du site du cours. Si vous êtes sur un autre os que windowsil suffit de suivre les instructions du site http://renaud-detry.net/teaching/flask/installation.html. Nous rappelons ici les instructions pour windows ::
py -3 -m venv venv (pour créer l'environnement)
venv\Scripts\activate (pour l'activer)

3 .Installer les packages utiles au bon fonctionnement du site par la commande
pip install -r requirements.txt

4. Initialiser la base de données
python flask/Base_de_donnee/Base.py

5.Lancer le site par les commandes

Pour Windows:
> set FLASK_APP=flaskr
> flask run

Pour Linux et Mac:
$ export FLASK_APP=flask
$ flask run

Suite à ces commandes, vous obtiendrez un lien qui viendra à vous directement dans le terminal.
Vous le Copiez-Coller dans un navigateur internet et vous verrez apparaitre notre site.

Structure du dépôt:

Dans le dossier capture d'écran :
- Les captures d’écran du site et des pages annexes qui affichent les graphes

Dans le dossier flaskr:
-Tous les fichiers nécessaires au bon fonctionnement du site :
	Base_de_donnée
	Tests
	Templates
	Les fichiers statiques
	__init__.py
	db.py, base_de_données_sql.sql, base_de_données_sql.db, database.py
	show_graph.py

1.Dans le sous-dossier Base_de_données:
-Les fichiers en rapport avec la base de donnée

2.Dans le sous-dossier Tests:
-Tous les fichiers nécessaire aux différents tests qui s’appliquent sur nos codes.

3.Dans le sous-dossier templates et fichier statiques:
-Les templates sont tous les fichiers html nécessaire à l'application
-les fichiers statiques sont les fichiers .css qui sont chacuns raccordés à un fichier html correspondant

=>accueil.html et styleacceuil.css représentent la page principale
=>graph.html et stylegraph.css correspondent à la mise en page des graphes affichés

4.Le fichier __init__.py correspond à 'l'usine à application'. 

5.db.py, database.py, Base_de_donnée_sql.sql & Base_de_donnée_sql.db:
-db.py est un fichier python qui s'occupe de lier la base de donnée Base_de_donnée_sql.sql à l'application (dans __init__.py).
-database.py est le fichier qui crée la structure des tables de la base de donnée
-basa_de_donnée_sql.db est la base de donnée en question

6.show_graph.py:
-C'est le fichier qui s'occupe de montrer les graphes correspondant aux résultats des formulaires reçus via accueil.html. 
Il renvoie ces graphes en renvoyant vers graph.html

setup.py, MANIFEST.in & requirements.txt:
-Ce sont les fichiers qui servent à rendre le projet installable

Les contribueurs
Groupe P2_Vincent_5 :
- Noah Fraiture
- Lyse Grolaux
- Martin Melen
- Vincent Wuillaume

