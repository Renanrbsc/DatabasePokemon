from database import db

trainer_pokemons = db.Table(
                             "trainer_pokemons",
                             db.Column('trainer_id', db.String(36), db.ForeignKey('trainers.id')),
                             db.Column('pokemon_id', db.String(36), db.ForeignKey('pokemons.id'))
                             )


class Pokemon(db.Model):
    __tablename__ = "pokemons"

    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(length=100))
    type = db.Column(db.String(length=50))
    height = db.Column(db.Float())
    weight = db.Column(db.Float())
    category = db.Column(db.String(length=50))
    ability = db.Column(db.String(length=100))
    ability_two = db.Column(db.String(length=100))
    weakness = db.Column(db.String(length=50))
    weakness_two = db.Column(db.String(length=50))
    description = db.Column(db.String(length=255))

    trainers = db.relationship("Trainer", back_populates="pokemons", secondary=trainer_pokemons)

    def serialize(self):
        return {
                "id": self.id, 
                "name": self.name, 
                "type": self.type, 
                "height": self.height,
                "weight": self.weight, 
                "category": self.category, 
                "ability": self.ability,
                "ability_two": self.ability_two, 
                "weakness": self.weakness,
                "weakness_two": self.weakness_two, 
                "description": self.description
                }

    def __str__(self):
        return f"Code: {self.id} \n" \
               f"Name: {self.name} \n" \
               f"Type: {self.type} \n" \
               f"Height: {str(self.height) + ' m'} \n" \
               f"Weight: {str(self.weight) + ' kg'} \n" \
               f"Category: {self.category} \n" \
               f"Ability: {self.ability} \n" \
               f"Ability Two: {self.ability} \n" \
               f"Weakness: {self.weakness} \n" \
               f"Weakness Two: {self.weakness_two} \n" \
               f"Description: {self.description} \n"


