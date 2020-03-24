import random
from application import app, db
from application.models import deck

@app.route('/')
def reset():
    if str(deck.query.all()) != '[]':
        db.session.query(deck).delete()
        db.session.commit()
    suits = ["Hearts","Spades","Clubs","Diamonds"]
    cards=["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
    for suit in suits:
        value = 1
        for card in cards:
            value += 1
            carddata = deck(card = card, suit = suit, value = value)
            db.session.add(carddata)
            db.session.commit()
    return" TEST"            
