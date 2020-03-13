import random
def card():
    cards=["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
    randcard=cards[random.randint(0,13)]
    return randcard

"""

def draw(player):
    draw = 0
    while draw <1:
        randcard = random.randint(1,52)
        if str(db.query.filter(deck.id == randcard).all()) != '[]':
            card = deck.query.filter(deck.id == randcard).first()
            draw += 1
            hans = hands(player = player,cardname = card.name, suit = card.suit) 
            db.session.add(hand)
            db.session.delete(card)
            db.session.commit
            return card
draw(1)
draw(1)

"""

