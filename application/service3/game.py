from Flask import flask
from service1 import randcard
from service2 import randsuit
from application import app, db

@app.route('/', methods=['GET','POST'])
def home():
  return render_template('index.html', title='home')
