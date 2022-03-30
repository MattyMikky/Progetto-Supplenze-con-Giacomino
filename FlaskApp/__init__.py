
#!File da eseguire
#! C:\Users\matti\OneDrive\Desktop\Visual_Studio_Code_Projects\Progetto_Supplenze_con_Giacomino\FlaskApp
from flask import Flask


def create_app():
    app = Flask(__name__)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
