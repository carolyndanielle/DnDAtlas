from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    race = db.Column(db.String(50))
    character_class = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# Add other relevant fields and classes as needed
