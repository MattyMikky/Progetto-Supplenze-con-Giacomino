# C:\Users\matti\OneDrive\Desktop\Visual_Studio_Code_Projects\Progetto_Supplenze_con_Giacomino\Progetto_Supplenze_Flask
from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# bug: cercare di risolvere il problema del terminale di VS CODE

# TODO: continuare a fare il sito con bootstrap e capire come fare ad implementare il programma fatto da Giacomo

# !: spaccarsi assolutamaente di video e capire come fare ahahahah
