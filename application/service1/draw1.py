import random

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



