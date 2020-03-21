import random
from  sqlalchemy.sql.expression import func, select
from application import app, db
from application.models import deck
from flask import jsonify

def sqltojson(row):
    y = row.split()
    c = (y[2])
    s = (y[3].split(":")[1])
    v = (y[5])
    J  = { "Card:": c, "Suit:" : s, "Value:" : v }
    return J

@app.route('/')
def draw():
    if str(deck.query.all()) != '[]':
        card = db.session.query(deck).order_by(func.rand()).first()
        db.session.delete(card)
        db.session.commit()
        return jsonify(sqltojson(str(card)))
    return "TEST service 1"
