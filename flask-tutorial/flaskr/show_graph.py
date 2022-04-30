from fullmoon import IsFullMoon
import numpy as np
from PIL import Image
import os
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from flaskr.db import get_db

bp = Blueprint('graph', __name__, url_prefix='/graph')

def isSmaller(date, date2):
    """
    jour/mois/année
    :return: true si date apparait plus tôt dans l'annéée
    """
    parsed_date = date.split('/')
    parsed_date2 = date2.split('/')
    for i in range(1, 4):
        if int(parsed_date[-i]) != int(parsed_date2[-i]):
            return int(parsed_date[-i]) < int(parsed_date2[-i])
    return None


@bp.route('/graphs_lune', methods=('GET', 'POST'))
def get_graph_lune():
    date_debut = request.form['date_debut']
    date_fin = request.form['date_fin']
    famille = request.form['famille']

    db = get_db()
    error = None
    dic = lune(db, date_debut, date_fin, famille)
    label = "Période"
    keys = dic.keys()
    values = dic.values()
    if dic == {}:
        error = "Aucune donnée"

    if error is None:
        # TODO : afficher le graph avec le dic
        return render_template('graph.html', keys=keys, values=values, name=label)
    else: flash(error)
    return redirect(url_for('accueil'))

#  attention package fullmoon utilisé
def lune(cursor, debut, fin, famille_recherche=None):
    mooned = []
    unmooned = []
    i = IsFullMoon()
    for row in cursor.execute(
        'SELECT DATE, ID FROM VELAGES'
    ):
        date = row[0]
        ID = row[1]
        if famille_recherche:
            famille = cursor.execute(
                'SELECT NOM FROM FAMILLES WHERE ID = ?', (ID,)
            ).fetchone()
            if famille != famille_recherche: continue
        if not isSmaller(debut, date) or not isSmaller(date, fin): continue
        if i.set_date_string(date, '%d/%m/%y').is_full_moon():
            mooned.append(ID)
        else: unmooned.append(ID)
    return {'Pleine Lune':mooned, 'Lune incomplète':unmooned}

@bp.route('/graphs_velage', methods=('GET', 'POST'))
def get_graph_velage():
    date_debut = request.form['date_debut']
    date_fin = request.form['date_fin']
    famille = request.form['famille']

    db = get_db()
    error = None
    dic = velages(db, date_debut, date_fin, famille)
    label = "Période"
    keys = dic.keys()
    values = dic.values()
    if dic == {}:
        error = "Aucune donnée"

    if error is None:
        # TODO : afficher le graph avec le dic
        return render_template('graph.html', keys=keys, values=values, name=label)
    else:
        flash(error)
    return redirect(url_for('accueil'))

def velages(cursor, debut, fin, famille_recherche=None):

    counting = {}
    for row in cursor.execute(
        'SELECT DATE, ID FROM VELAGES'
    ):
        date = row[0]
        ID = row[1]
        if famille_recherche:
            famille = cursor.execute(
                'SELECT NOM FROM FAMILLES WHERE ID = ?', (ID,)
            ).fetchone()
            if famille != famille_recherche: continue
        if isSmaller(debut,date) and isSmaller(date,fin):
            counting[date] = counting.get(date, 0) + 1
    return counting

@bp.route('/graphs_races', methods=('GET', 'POST'))
def get_graph_races():
    races = request.form['races']
    pourcentage = request.form['pourcentage']

    db = get_db()
    error = None
    dic = show_races(db, races, pourcentage)
    label = "Races"
    keys = dic.keys()
    values = dic.values()
    if dic == {}:
        error = "Aucune donnée"

    if error is None:
        # TODO : afficher le graph avec le dic
        return render_template('graph.html', keys=keys, values=values, name=label)
    else:
        flash(error)
    return redirect(url_for('accueil'))

def show_races(cursor, races, pourcentage):
    """
    :param cursor: acces to database
    :param races: wanted races
    :param pourcentage: pourcentage minimum des races affichées
    :return:
    """
    counting_race = {}
    for row in cursor.execute(
        'SELECT POURCENTAGE, TYPE_ID FROM ANIMAUX_TYPES'
    ):
        if int(row[0]) >= pourcentage and row[1] in races:
            counting_race = counting_race.get(row[1],0) + 1
    return counting_race

def recolor(image):

    def get_rapport(pixels: list):
        rapport = [0, 0, 0]
        somme = sum(pixels)
        for i in range(3):
            rapport[i] = pixels[i] / somme
        return rapport

    def recolor(im, rapport_couleur):
        im_pixel = np.array(im)
        longueur, hauteur = im.size
        recolored_im = Image.new(mode="RGBA", size=(longueur, hauteur))
        recolored_im_pixel = np.array(recolored_im)
        for y in range(len(im_pixel)):
            for x in range(len(im_pixel[0])):
                if im_pixel[y][x][3] == 0:
                    continue

                norme = np.linalg.norm(im_pixel[y][x][:2])
                new_color = np.multiply(norme, rapport_couleur)
                new_color = np.clip(new_color, 0, 255)
                recolored_im_pixel[y][x] = np.append(new_color, im_pixel[y][x][3])
        return Image.fromarray(recolored_im_pixel)

    list_possible_color = ((31,255,243), (255,49,31), (255,61,31), (173,13,129), (153,195,151))
    color = np.random.choice(list_possible_color)
    rapport = get_rapport(color)
    recolored = recolor(image, rapport)
    return recolored

def merge():
    pass

image = Image.open(r'image\vache.png').convert('RGBA')
recolor(image)