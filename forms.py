from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

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

class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    organizer = StringField('Organizer', validators=[DataRequired()])
    event_type = StringField('Event Type', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
