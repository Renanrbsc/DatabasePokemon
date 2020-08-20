from database import db

trainers_pokemons = db.Table("trainers_pokemons",
                             db.Column('trainer_id', db.String(36), db.ForeignKey('trainers.id')),
                             db.Column('pokemon_id', db.String(36), db.ForeignKey('pokemons.id'))
                             )


class Trainer(db.Model):
    __tablename__ = "trainers"

    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(length=100))
    lastname = db.Column(db.String(length=100))
    age = db.Column(db.Integer)
    city = db.Column(db.String(length=100))

    pokemons = db.relationship("Pokemon", back_populates="trainers", secondary=trainers_pokemons)

    def serialize(self):
        return {
                "id": self.id,
                "name": self.name,
                "lastname": self.lastname,
                "age": self.age,
                "city": self.city,
                "pokemons": [pokemon.name for pokemon in self.pokemons]
                }

    def __str__(self):
        return f"Code: {self.id} \n" \
               f"Name: {self.name} \n" \
               f"Lastname: {self.lastname} \n" \
               f"Age: {self.age} \n" \
               f"City: {self.city} \n"
