import random
from flask  import jsonify
from application import app

@app.route('/')
def prize():
  randprize = random.randint(0,50)
  prizejson = { "Prize": randprize }
  return jsonify(prizejson)
