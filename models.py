from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    history = db.Column(db.String(1000), nullable=True)
    activities = db.Column(db.String(1000), nullable=True)
    relationship = db.Column(db.String(1000), nullable=True)
    special_needs = db.Column(db.String(1000), nullable=True)
    adoption_reason = db.Column(db.String(1000), nullable=True)
    terms = db.Column(db.String(1000), nullable=True) 
    button_link = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    age = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    adopted = db.Column(db.String(5), nullable=True)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    organizer = db.Column(db.String(100), nullable=False)
    event_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)

class Shelter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    opening_hours = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)

class Adoption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False) 
    name = db.Column(db.String(500), nullable=False)
    shelter = db.Column(db.String(100), nullable=False)
    animal = db.Column(db.String(100), nullable=False)
    birthdate = db.Column(db.String(10), nullable=False)
    ocupation = db.Column(db.String(30), nullable=False)
    income = db.Column(db.String(20), nullable=False)
    experience = db.Column(db.String(10), nullable=False)
    story = db.Column(db.String(1000), nullable=True)

class Curiosity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    picture = db.Column(db.String(100), nullable=True)
    content = db.Column(db.Text, nullable=False)

