from database import db
from app.domains.pokemons.models import trainer_pokemons


class Trainer(db.Model):
    __tablename__ = "trainers"

    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(length=100))
    lastname = db.Column(db.String(length=100))
    age = db.Column(db.Integer)
    city = db.Column(db.String(length=100))
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'))

    users = db.relationship("User", back_populates="trainers")
    pokemons = db.relationship("Pokemon", back_populates="trainers", secondary=trainer_pokemons)

    def serialize(self):
        return {
                "id": self.id,
                "name": self.name,
                "lastname": self.lastname,
                "age": self.age,
                "city": self.city,
                "pokemons": [pokemon.name for pokemon in self.pokemons],
                "user": self.users.serialize()
                }

    def __str__(self):
        return f"Code: {self.id} \n" \
               f"Name: {self.name} \n" \
               f"Lastname: {self.lastname} \n" \
               f"Age: {self.age} \n" \
               f"City: {self.city} \n"
