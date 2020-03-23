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
    return render_template('index.html')

@app.route('/draw/')
def draw():
    response = requests.get('http://draw:5000/').json()
    return render_template('index.html',card0 = response["Card0"], suit0 = response ["Suit0"], card1 = response["Card1"], suit1 = response ["Suit1"] )

@app.route('/prize/')
def prize():
    response = requests.get('http://prize:5002/').json()
    return response
