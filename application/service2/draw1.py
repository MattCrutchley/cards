import random

draw = 0
while draw <1:
    randcard = random.randint(1,52)
    if str(deck.query.filter(deck.id == randcard).all()) != '[]'
        card1 = deck.query.filter(deck.id == randcard).first()
        draw += 1
        return card1

db.session.delete(card1)
db.session.commit

while draw <2:
    randcard = random.randint(1,52)
    if str(deck.query.filter(deck.id == randcard).all()) != '[]'
        card2 = deck.query.filter(deck.id == randcard).first()
        draw += 1
        return card2
db.session.delete(card2)
db.session.commit


