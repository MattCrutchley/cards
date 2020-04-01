from application import db
from sqlalchemy import Table, Column, Integer, ForeignKey

class deck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card = db.Column(db.String(10))
    suit = db.Column(db.String(10))
    value = db.Column(db.Integer)

    def __repr__(self):
        return ''.join(['id:',str(self.id),'\r\n'
            'card: ', self.card,'\r\n', 'suit:', str(self.suit), '\r\n','value: ', str(self.value)])

