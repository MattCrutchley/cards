import random
from  sqlalchemy.sql.expression import func
from application import app, db
from application.models import deck

"""
def card():
    cards=["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
    return cards[random.randint(0,12)]

"""

def draw():
    if str(db.query.all()) != '[]':
        card = deck.order_by(func.rand()).first()
        db.session.delete(card)
        db.session.commit
        return "TEST service 1"
"""

test=["a","b","c","d"]
#print(test[3])
print(card())
"""