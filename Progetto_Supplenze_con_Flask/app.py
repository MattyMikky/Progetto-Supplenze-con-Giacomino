from flask import Flask, render_template
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    return app

# !: Continuare assolutamente sta ozzac di web app ma soprattuto capire come farla e
# !: soprattuto capire come implementare il programma che ha fatto Giacomo
