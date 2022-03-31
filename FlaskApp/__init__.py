
#!File da eseguire
#! C:\Users\matti\OneDrive\Desktop\Visual_Studio_Code_Projects\Progetto_Supplenze_con_Giacomino\FlaskApp
from flask import Flask, Blueprint, render_template, url_for


app = Flask(__name__)


@app.route('/')
def base():
    return render_template('base.html')
