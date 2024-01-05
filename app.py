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
    description = db.Column(db.String(255), nullable=False)
    button_link = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    age = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(50), nullable=False)

class AnimalForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    button_link = StringField('Button Link', validators=[DataRequired()])
    type = StringField('Type', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])

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
    print(animals)
    return render_template('index.html', animals=animals)

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
    print(animals)
    return render_template('index.html', animals=animals)

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
    return render_template('events.html')

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
