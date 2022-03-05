from email.policy import default
from unicodedata import category
from pokemons import db

class Pokemon(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    poke_name = db.Column(db.String(20), nullable=False)
    poke_type = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    img_name = db.Column(db.String(50), default='default.png')

    def __repr__(self):
        return "<Pokemon: {}>".format(self.poke_name)

    def as_dict(self):
        return {
            'id': self.id,
            'poke_name': self.poke_name,
            'poke_type': self.poke_type,
            'img_name': self.img_name
        }