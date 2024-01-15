from flask import Flask, render_template, redirect, url_for, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_migrate import Migrate
from flask_mail import Mail, Message
import markdown

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Petify.db'
db = SQLAlchemy(app)
admin = Admin(app, name='Admin', template_mode='bootstrap3')
migrate = Migrate(app, db)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'petify.adoption@gmail.com'
app.config['MAIL_PASSWORD'] = 'cuge vmcz gwzs dfpa'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

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
    adopted = db.Column(db.String(100), nullable=True)

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
    adopted = StringField('Adopted', validators=[DataRequired()])

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
    email_address = db.Column(db.String(100), nullable=True)

class ShelterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    opening_hours = StringField('Opening Hours', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    email_address = StringField('Email address', validators=[DataRequired()])

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

class AdoptionForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    shelter = StringField('Shelter', validators=[DataRequired()])
    animal = StringField('Animal', validators=[DataRequired()])
    birthdate = StringField('Date of birth', validators=[DataRequired()])
    ocupation = StringField('Ocupation', validators=[DataRequired()])
    income = StringField('Income', validators=[DataRequired()])
    experience = StringField('Experience', validators=[DataRequired()])
    story = StringField('Story', validators=[DataRequired()])

class Curiosity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    picture = db.Column(db.String(100), nullable=True)
    content = db.Column(db.Text, nullable=False)

class CuriosityForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    picture = StringField('Picture', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])

class AnimalAdminView(ModelView):
    column_searchable_list = ['name', 'type', 'location']
    form_excluded_columns = ['id']

class EventAdminView(ModelView):
    column_searchable_list = ['title', 'event_type', 'location']
    form_excluded_columns = ['id']

class ShelterAdminView(ModelView):
    column_searchable_list = ['name', 'location', 'email_address']
    form_excluded_columns = ['id']

class AdoptionAdminView(ModelView):
    column_searchable_list = ['username', 'shelter', 'animal']
    form_excluded_columns = ['id']

class CuriosityAdminView(ModelView):
    column_searchable_list = ['title']
    form_excluded_columns = ['id']

admin.add_view(AnimalAdminView(Animal, db.session))
admin.add_view(EventAdminView(Event, db.session))
admin.add_view(ShelterAdminView(Shelter, db.session))
admin.add_view(AdoptionAdminView(Adoption, db.session))
admin.add_view(CuriosityAdminView(Curiosity, db.session))

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
    cities = [shelter.location.split(',')[-1] for shelter in Shelter.query.all()]
    print(animals)
    return render_template('index.html', animals=animals, shelters=shelters, cities = cities)


@app.route('/<category_name>')
def category_page(category_name):
    category = Animal.query.filter_by(name=category_name).first()
    if category:
        return render_template('category_page.html', category=category)
    else:
        return render_template('404.html')

@app.route('/facts.html')
def list_curiosities():
    curiosities = Curiosity.query.all()
    return render_template('facts.html', curiosities=curiosities)

@app.route('/fact/<fact_name>')
def fact_page(fact_name):
    curiosity = Curiosity.query.filter_by(title=fact_name).first()
    if curiosity:
        content_html = markdown.markdown(curiosity.content)
        page_title = curiosity.title
        home_text = 'Curiozitati'
        current_page = fact_name
        background_image_url = url_for('static', filename='img/' + curiosity.picture)
        return render_template('fact_page.html', curiosity=curiosity, content_html=content_html, page_title=page_title, home_text=home_text, current_page=current_page, background_image_url=background_image_url)
    else:
        return render_template('404.html')

@app.route('/search_results')
def search_results():
    shelters = Shelter.query.all()
    cities = [shelter.location.split(',')[-1] for shelter in Shelter.query.all()]
    try:
        animal_type = request.args.get('animal_type')
        age = request.args.get('age')
        animal_location = request.args.get('location')

        filtering_results = Animal.query.filter(
        and_(
        (not animal_type or Animal.type == animal_type),
        (not age or Animal.age == age),
        (not animal_location or Animal.location.like(f"%{animal_location}%"))
        )
        ).all()

        return render_template('index.html', animals=filtering_results, shelters = shelters, cities = cities)
    except Exception as e:
        print(str(e))
        abort(500)

@app.route('/index.html')
def index2():
    animals = Animal.query.all()
    shelters = Shelter.query.all()
    cities = [shelter.location.split(',')[-1] for shelter in Shelter.query.all()]
    return render_template('index.html', animals=animals, shelters=shelters, cities = cities)

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
    shelters = Shelter.query.all()
    return render_template('contact.html', shelters = shelters)

@app.route('/contact_shelter', methods=['POST'])
def contact_shelter():
    shelters = Shelter.query.all()
    form_name = request.form['name']
    form_email = request.form['email']
    form_shelter = request.form['shelter']
    form_subject = request.form['subject']
    form_text = request.form['text']
    shelter = Shelter.query.filter_by(name=form_shelter).first()
    receiver = shelter.email_address
    try:
        msg = Message(form_subject, sender='petify.adoption@gmail.com', recipients=[receiver])
        msg.body = 'De la ' + form_name + ',' + form_email + '\n' + form_text
        mail.send(msg)
        print('EMAIL SENT SUCCESSFULLY!', 'success')
    except Exception as e:
        print(f'EMAIL ERROR: {str(e)}', 'error')
    return redirect(url_for('index'))

@app.route('/ask_question', methods=['POST'])
def ask_question():

    form_name = request.form['name']
    form_email = request.form['email']
    form_subject = 'New Question from Petify Website'
    form_text = request.form['question']
    receiver = "micleamadalinasofia@gmail.com"

    try:
        msg = Message(form_subject, sender='petify.adoption@gmail.com', recipients=[receiver])
        msg.body = f'From: {form_name}, {form_email}\n\nQuestion: {form_text}'
        mail.send(msg)
        print('EMAIL SENT SUCCESSFULLY!', 'success')
    except Exception as e:
        print(f'EMAIL ERROR: {str(e)}', 'error')

    return redirect(url_for('index'))

@app.route('/add_curiosity', methods=['GET', 'POST'])
def add_curiosity():
    form = CuriosityForm()
    facts = Curiosity.query.all()

    if form.validate_on_submit():
        new_curiosity = Curiosity(
            title=form.title.data,
            content=form.content.data
        )
        db.session.add(new_curiosity)
        db.session.commit()
        return redirect(url_for('add_curiosity'))

    return render_template('add_curiosity.html', form=form, facts=facts)


@app.route('/questions', methods=['GET'])
def questions_page():
    return render_template('questions.html')

@app.route('/events.html')
def events():
    events = Event.query.all()
    print(events)
    return render_template('events.html', events=events)

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

# WORK IN PROGRESS: SA IAU NUMELE USERULUI LOGAT!!!!
@app.route('/adoption_completed', methods= ['POST'])
def adoption_completed():
     user = "nume user logat"
     form_name = request.form['name']
     form_bday = request.form['bday']
     form_ocupation = request.form['ocupation']
     form_income = request.form['income']
     form_experience = request.form['experience']
     form_story = request.form['experienceStory']
     form_shelter = request.form['shelter']
     form_animal = request.form['animal']

     new_adoption = Adoption(
        username = user,
        name = form_name,
        shelter = form_shelter,
        animal = form_animal,
        birthdate = form_bday,
        ocupation = form_ocupation, 
        income = form_income, 
        experience = form_experience,
        story = form_story
     )
     db.session.add(new_adoption)
     db.session.commit()
     print("ADOPTIA S A SALVAT")

     adopted_animal = Animal.query.filter_by(name = form_animal).first()
     adopted_animal.adopted = user
     db.session.commit()
     print("ANIMALUL MARCAT CA ADOPTAT")

     return redirect(url_for('index'))
     

# cale ca sa generez animalele de la adapostul selectat
@app.route('/animals_from_shelter/<shelter_name>')
def get_animals_for_shelter(shelter_name):
    animals = Animal.query.filter_by(location=shelter_name, adopted='false').all()
    animals_data = [{'name': animal.name} for animal in animals]
    return jsonify({'animals': animals_data})

@app.route('/adoption.html')
def adoption_form():
    shelters = Shelter.query.all()
    return render_template('adoption.html', shelters = shelters)

@app.route('/adopt_animal')
def adopt_from_button():
    try:
        animal_name = request.args.get("animal_name")
        print(animal_name)
        selected_animal = Animal.query.filter_by(name=animal_name).first()
        return render_template("adoption.html", animal = selected_animal)
    except Exception as e:
        print(str(e))
        abort(500)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)