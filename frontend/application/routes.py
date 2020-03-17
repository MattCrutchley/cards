import random
from application import app, db
from application.models import deck
from flask import render_template
import requests
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reset/')
def reset():
    response = requests.get('http://reset:5001/')
    return "reset test"

@app.route('/draw/')
def draw():
    response = requests.get('http://draw:5000/').json()
    return render_template('index.html',card = response["card"])
