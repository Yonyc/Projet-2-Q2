import os
import pathlib
from flask import Flask, render_template



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(pathlib.Path(__file__).parent.absolute(), "Base_de_donnee/Base_de_donne_sql.db")
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # affiche la page principale 
    @app.route('/')
    def accueil():
        return render_template('accueil.html')
    
    #importe le fichier db.py qui permet de lier la base de donnée à 'l'usine à application'
    import db
    db.init_app(app)
    
    #importe le fichier show_graph.py qui permet de renvoyer le graphe correspondant aux outputs des formulaires html
    import show_graph
    app.register_blueprint(show_graph.bp)
    
    return app
