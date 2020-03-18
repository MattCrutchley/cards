import random
from  sqlalchemy.sql.expression import func, select
from application import app, db
from application.models import deck
from flask import jsonify

"""
def card():
    cards=["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
    return cards[random.randint(0,12)]



@app.route('/draw')
def draw():
    if str(deck.query.all()) != '[]':
        rand = random.randrange(0, db.session.query(deck).count()) 
        card = db.session.query(deck)[rand].first()
        db.session.delete(card)
        db.session.commit()
        return str(card)
    return "TEST service 1"

"""

import decimal, datetime
# reformats nubers returned as dates
def alchemyencoder(obj):
    """JSON encoder function for SQLAlchemy special classes."""
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)

@app.route('/')
def draw():
    if str(deck.query.all()) != '[]':
        card = db.session.query(deck).order_by(func.rand()).first()
        db.session.delete(card)
        db.session.commit()
        lcard = str(card).split(",")
        return jsonify({"id":lcard[0],"card":lcard[1],"suit":lcard[2],"value":lcard[3]})
    return "TEST service 1"

