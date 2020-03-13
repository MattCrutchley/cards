import random
def suit():
    suits = [Hearts,Spades,Clubs,Diamonds]
    randsuit = suits[random.randint(0,4)]
    return randsuit
