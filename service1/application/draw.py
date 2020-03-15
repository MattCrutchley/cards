import random
def card():
    cards=["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
    return cards[random.randint(0,12)]

"""

def draw():
    draw = 0
    while draw <1:
        randcard = random.randint(1,52)
        if str(db.query.filter(deck.id == randcard).all()) != '[]':
            card = deck.query.filter(deck.id == randcard).first()
            draw += 1
            db.session.delete(card)
            db.session.commit
            return card

"""

test=["a","b","c","d"]
#print(test[3])
print(card())