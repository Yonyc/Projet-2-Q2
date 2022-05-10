import sqlite3
import os
import pathlib
from Heritage_genetique import creation_race

def main():

    # On établi une connection à la base de donnée
    db = sqlite3.connect(os.path.join(pathlib.Path(__file__).parent.absolute(), "Base_de_donne_sql.db"))
    cursor = db.cursor()

    # On ouvre le script sql qui va permettre de créer la table de données
    with open(os.path.join(pathlib.Path(__file__).parent.absolute(), "database.sql")) as f:
        db_Base = f.read()

    # On exécute le script sql
    cursor.executescript(db_Base)
    db.commit()

    ajouter_données = ["insert_animaux.sql", "insert_animaux_types.sql", "insert_animaux_velages.sql", "insert_complications.sql", "insert_familles.sql", "insert_types.sql", "insert_velages.sql", "insert_velages_complications.sql"]

    # On lit les fichiers à ajouter dans la base de donnée
    for nouveau_fichier in ajouter_données:
        with open(os.path.join(pathlib.Path(__file__).parent.absolute(), f"./1002-sql-data/{nouveau_fichier}")) as f:
            ajou_contenu = f.read()
        
        # On insert les données
        cursor.executescript(ajou_contenu)
        db.commit()

    # On ajoute la fonction permettant de calculer l'héritage d'une vache grâce à ses ancêtres
    creation_race(db)

    db.close()

if __name__ == '__main__':
    main()
