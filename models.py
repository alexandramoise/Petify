from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    button_link = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    age = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(50), nullable=False)

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

