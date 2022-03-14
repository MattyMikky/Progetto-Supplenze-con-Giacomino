#C:\Users\matti\OneDrive\Desktop\Visual Studio Code Projects\Progetto Supplenze con Giacomino\Progetto_Supplenze_Flask
from flask import Flask, render_template, request, flash


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

    
 