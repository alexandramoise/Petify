from flask import Flask, render_template
from flask import request

app = Flask(__name__)

categories = [
    {"name": "Pisicuță", "image": "cat-1.jpg", "description": "Pisicuță adorabilă.", "button_link": "/cat_page.html", "type": "Pisică", "age": "Pui", "location": "Oraș 1"},
    {"name": "Cățel", "image": "dog-1.jpg", "description": "Cățel prietenos și jucăuș.", "button_link": "/dog_page.html", "type": "Câine", "age": "Pui", "location": "Oraș 2"},
    {"name": "Pisică", "image": "cat-2.jpg", "description": "Pisică pufoasă", "button_link": "/cat_page.html", "type": "Pisică", "age": "Adult", "location": "Oraș 1"},
    {"name": "Câine", "image": "dog-2.jpg", "description": "Câine loial și jucăuș", "button_link": "/dog_page.html", "type": "Câine", "age": "Adult", "location": "Oraș 2"},
    {"name": "Papagal", "image": "parrot-1.jpg", "description": "Papagal colorat.", "button_link": "/dog_page.html", "type": "Papagal", "age": "Pui", "location": "Oraș 1"},
    # ... alte categorii
]

# Ruta pentru pagina de start
@app.route('/')
def index():
    return render_template('index.html', categories=categories)

# Ruta dinamică pentru fiecare categorie de animal
@app.route('/<category_name>')
def category_page(category_name):
    # Găsește categoria corespunzătoare
    category = next((c for c in categories if c['name'].lower() == category_name.lower()), None)
    if category:
        return render_template('category_page.html', category=category)
    else:
        # Poți trata cazul în care categoria nu există, de exemplu, afișând o pagină de eroare sau redirectând către altă pagină
        return render_template('category_not_found.html', category_name=category_name)
            
@app.route('/search_results')
def search_results():
    try:
        animal_type = request.args.get('animal_type')
        age = request.args.get('age')
        location = request.args.get('location')
        print(f'Argumente: ',{animal_type}, {age}, {location})
        
        # Filtrare după parametrii de căutare și obținere de rezultate din lista de animale
        filtered_animals = [animal for animal in categories if
                            (not animal_type or animal.get('type') == animal_type) and
                            (not age or animal.get('age') == age) and
                            (not location or animal.get('location') == location)]
        
        filtering_results = []
        for animal in categories:
            if((not animal_type or animal.get("type") == animal_type)
             and (not age or animal.get("age") == age)
             and (not location or animal.get("location") == location)):
                filtering_results.append(animal)

        
        for el in filtering_results:
            print(f'la filtrare apare: ', el)
        
        return render_template('index.html', categories=filtering_results)
    except Exception as e:
        # Afișează detalii despre eroare în consolă
        print(str(e))
        # Oferă un răspuns HTTP de eroare 500
        abort(500)

@app.route('/index.html')
def index2():
    return render_template('index.html', categories=categories)

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
    app.run(debug=True)
