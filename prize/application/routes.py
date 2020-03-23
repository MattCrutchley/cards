import random
import jsonify
from application import app

@app.route('/')
def prize():
  randprize = random.randint(50,100)
  prizejson = { "Prize": randprize }
  return jsonify(prizejson)
