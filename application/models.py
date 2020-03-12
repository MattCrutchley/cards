from application import db
from sqlalchemy import Table, Column, Integer, ForeignKey
from flask_login import UserMixin


class deck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardname = db.Column(db.String(10), nullable=False)
    suit = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return ''.join([
            'id:',str(self.id),'card: ', self.cardname, 'suit', self.suit, '\r\n',
            ])


class hands(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card = db.Column(db.String(10), nullable=False)
    suit = db.Column(db.String(10), nullable=False)
    player = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return ''.join([
            'id:',str(self.id),'card: ', self.cardname,'\r\n', 'suit', self.suit, '\r\n', 'player:',self.player])
    
    
