import random
"""
def suit():
    suits = [Hearts,Spades,Clubs,Diamonds]
    return randsuit suits[random.randint(0,3)]
"""

@app.route('/reset')
def reset()
    if str(deck.query.all() != '[]'):
        deckdata = deck.query.all
        db.session.delete(deckdata)
        db.session.commit()
    suits = [Hearts,Spades,Clubs,Diamonds]
    cards={"2","3","4","5","6","7","8","9","10","J","K","Q","A"]
    for suit in suits:
    value = 1
        for card in cards:
            value += 1
            carddata = cards(card = card, suit = suit value = value)
            db.session.add(carddata)
            db.session.commit()
    return" TEST"            
