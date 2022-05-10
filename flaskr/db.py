import sqlite3
import pathlib
import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect("Base_de_donnee/Base_de_donne_sql.db")
        g.db.row_factory =sqlite3.Row
    print(g.db)
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
        
def init_app(app):
    app.teardown_appcontext(close_db)
