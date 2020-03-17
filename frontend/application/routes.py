import random
from application import app, db
from application.models import deck

@app.route('/')
def index():
    return render_template('index.html')
