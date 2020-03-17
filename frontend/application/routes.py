import random
from application import app, db
from application.models import deck
from Flask import flask, render template

@app.route('/')
def index():
    return render_template('index.html')
