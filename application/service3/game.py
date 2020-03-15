from Flask import flask
from service1 import randcard
from service2 import randsuit
from application import app, db
import random

@app.route('/', methods=['GET','POST'])
def home():
  yourcard = service1.randcard()
  yoursuit = service2.randsuit()
  opponentcard = service1.randcard()
  opponentsuit = service2.randsuit()
  prize = "£"+str(random.randint(50,100))
  return render_template('index.html', title='home')
