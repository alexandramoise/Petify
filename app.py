from flask import Flask, render_template, redirect, url_for, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Petify.db'
db = SQLAlchemy(app)
admin = Admin(app, name='Admin', template_mode='bootstrap3')
migrate = Migrate(app, db)

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

class AnimalForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    history = StringField('History', validators=[DataRequired()])
    activities = StringField('Activities', validators=[DataRequired()])
    relationship = StringField('Relationship', validators=[DataRequired()])
    special_needs = StringField('Special Needs', validators=[DataRequired()])
    adoption_reason = StringField('Adoption Reason', validators=[DataRequired()])
    terms = StringField('Terms', validators=[DataRequired()])
    button_link = StringField('Button Link', validators=[DataRequired()])
    type = StringField('Type', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    organizer = db.Column(db.String(100), nullable=False)
    event_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)

class EventForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    organizer = StringField('Organizer', validators=[DataRequired()])
    event_type = StringField('Event Type', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])

class Shelter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    opening_hours = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(50), nullable=False)

class ShelterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    opening_hours = StringField('Opening Hours', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])

class AnimalAdminView(ModelView):
    column_searchable_list = ['name', 'type', 'location']
    form_excluded_columns = ['id']

class EventAdminView(ModelView):
    column_searchable_list = ['title', 'event_type', 'location']
    form_excluded_columns = ['id']

class ShelterAdminView(ModelView):
    column_searchable_list = ['name', 'location']
    form_excluded_columns = ['id']

admin.add_view(AnimalAdminView(Animal, db.session))
admin.add_view(EventAdminView(Event, db.session))
admin.add_view(ShelterAdminView(Shelter, db.session))

@app.route('/add_animal', methods=['GET', 'POST'])
def add_animal():
    form = AnimalForm()
    animals = Animal.query.all()

    if form.validate_on_submit():
        new_animal = Animal(
            name=form.name.data,
            image=form.image.data,
            description=form.description.data,
            button_link=form.button_link.data,
            type=form.type.data,
            age=form.age.data,
            location=form.location.data
        )
        db.session.add(new_animal)
        db.session.commit()
        return redirect(url_for('add_animal'))

    return render_template('add_animal.html', form=form, animals=animals)

@app.route('/')
def index():
    animals = Animal.query.all()
    shelters = Shelter.query.all()
    print(animals)
    return render_template('index.html', animals=animals, shelters=shelters)


@app.route('/<category_name>')
def category_page(category_name):
    category = Animal.query.filter_by(name=category_name).first()
    if category:
        return render_template('category_page.html', category=category)
    #else:
        #return render_template('category_not_found.html', category_name=category_name)


@app.route('/search_results')
def search_results():
    try:
        animal_type = request.args.get('animal_type')
        age = request.args.get('age')
        location = request.args.get('location')

        filtering_results = Animal.query.filter(
            (not animal_type or Animal.type == animal_type) &
            (not age or Animal.age == age) &
            (not location or Animal.location == location)
        ).all()

        return render_template('index.html', animals=filtering_results)
    except Exception as e:
        print(str(e))
        abort(500)

@app.route('/index.html')
def index2():
    animals = Animal.query.all()
    shelters = Shelter.query.all()
    print(animals)
    return render_template('index.html', animals=animals, shelters=shelters)

@app.route('/add_event', methods=['GET', 'POST'])
def add_event():
    form = EventForm()
    events = Event.query.all()

    if form.validate_on_submit():
        new_event = Event(
            title=form.title.data,
            image=form.image.data,
            location=form.location.data,
            organizer=form.organizer.data,
            event_type=form.event_type.data,
            description=form.description.data
        )
        db.session.add(new_event)
        db.session.commit()
        return redirect(url_for('add_event'))

    return render_template('add_event.html', form=form, events=events)

@app.route('/add_shelter', methods=['GET', 'POST'])
def add_shelter():
    form = ShelterForm()
    shelters = Shelter.query.all()

    if form.validate_on_submit():
        new_shelter = Shelter(
            name=form.name.data,
            opening_hours=form.opening_hours.data,
            location=form.location.data
        )
        db.session.add(new_shelter)
        db.session.commit()
        return redirect(url_for('add_shelter'))

    return render_template('add_shelter.html', form=form, shelters=shelters)

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/adoption.html')
def adoption_form():
    return render_template('adoption.html')

@app.route('/events.html')
def events():
    events = Event.query.all()
    print(events)
    return render_template('events.html', events=events)

@app.route('/facts.html')
def facts():
    return render_template('facts.html')

@app.route('/questions.html')
def questions():
    return render_template('questions.html')

@app.route('/register.html')
def register():
    return render_template('register.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/category.html')
def category():
    return render_template('category.html')


""" @app.route('/job-detail.html')
def job_detail():
    return render_template('job-detail.html')

@app.route('/job-list.html')
def job_list():
    return render_template('job-list.html')

@app.route('/testimonial.html')
def testimonial():
    return render_template('testimonial.html')

@app.route('/404.html')
def error():
    return render_template('404.html')
 """


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
