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
    response = requests.get('https://reset:5001/')
    return "reset test"
