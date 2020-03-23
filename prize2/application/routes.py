import random
from flask  import jsonify
from application import app

@app.route('/')
def prize():
  randprize = random.randint(51,100)
  prizejson = { "Prize": randprize }
  return jsonify(prizejson)
