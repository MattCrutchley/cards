import random
from  sqlalchemy.sql.expression import func, select
from application import app, db
from application.models import deck
from flask import jsonify

def sqltojson(row,x):
    y = row.split()
    c = (y[2])
    s = (y[3].split(":")[1])
    v = (y[5])
    J  = { "Card{}".format(x): c, "Suit{}".format(x) : s, "Value{}".format(x) : v }
    return J

@app.route('/')
def draw():
    for i in range(2):
        if str(deck.query.all()) != '[]':
            card = db.session.query(deck).order_by(func.rand()).first()
            db.session.delete(card)
            db.session.commit()       
            handjson = {}
            handjson.update(sqltojson(str(card),str(i))          
    return jsonify(handjson)
