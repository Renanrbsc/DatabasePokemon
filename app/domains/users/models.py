from database import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(length=50))
    password = db.Column(db.String(length=50))
    email = db.Column(db.String(length=100))
    active = db.Column(db.Boolean, default=True)

    trainers = db.relationship("Trainer", uselist=False, back_populates="users")

    def serialize(self):
        return {
                "id": self.id,
                "Username": self.username,
                "Password": self.password,
                "Email": self.email,
                "Active": self.active
                }

    def __str__(self) -> str:
        return f"id: {self.id} \n" \
               f"Username: {self.username} \n" \
               f"Password: {self.password} \n" \
               f"Email: {self.email} \n" \
               f"Active: {self.active} \n"

