from gettext import find
import sqlite3
from typing import List, Tuple, Dict

# Une liste de tout les identifiants des vaches
def vaches(db: sqlite3.Connection):
    with db as cursor:
        return cursor.execute("SELECT id FROM animaux").fetchall()

# Une liste de l'identifiant des races et le pourcentage des vaches si les données sont déjà présente. 
def races_vache(db: sqlite3.Connection, id_: int):
    with db as cursor:
        return cursor.execute("SELECT type_id, pourcentage FROM animaux_types WHERE animal_id = ?", (id_)).fetchall()

# Liste des identifiants de tout les parents.
def parents(db: sqlite3.Connection, id_: int):
    with db as cursor:
        return cursor.execute("SELECT pere_id, mere_id FROM animaux, animaux_velages, velages WHERE animaux.id = ? AND animaux.id = animaux_velages.animal_id AND animaux_velages.velages_id =velages.id = velage.id", (id_)).fetchone()

# Calcule le pourcentage de la race d'une vache grâce à la race des parents.
def calcule_pourcentage_races(parents_races: List[Tuple[int, float]]):
    races_dict: Dict[int, float] = {}
    for race in parents_races:
        races_dict [race[0]] = races_dict.get(race[0], 0) + race[1]
    return [(race[0], race[1]/2) for race in races_dict.items()]

# Ajout des races des vaches dans la base de donnée
def ajout_race(db: sqlite3.Connection, animal_id, races: List[Tuple[int, float]]):
    for race in races:
        with db as cursor:
            cursor.execute("INSERT INTO animaux_types VALUES (?, ?, ?)", (animal_id, race[0], race[1]))

# Calcule et ajoute le pourcentage de la race d'une vache si celui-ci n'est pas dans la base de donnée.
def find_race(db: sqlite3.Connection, animal_id: int):
    pere, mere = parents(db, animal_id)
    race_mere = List[Tuple[int, float]] = races_vache(db, mere)
    race_pere = List[Tuple[int, float]] = races_vache (db, pere)

    if not len(race_mere):
        race_mere: List[Tuple[int, float]] = find_race(db, mere)

    if not len(race_pere):
        race_pere: List[Tuple[int, float]]= find_race(db, pere)

    races: List[Tuple[int, float]] = calcule_pourcentage_races(race_mere + race_pere)

    ajout_race(db, animal_id, races)

def création_race(db: sqlite3.Connection):
    réponse: List[int] = vaches(db)
    for animal_id in réponse:
        if len(races_vache(db, animal_id)) == 0:
            find_race(db, animal_id)
