from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def index2():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/job-detail.html')
def job_detail():
    return render_template('job-detail.html')

@app.route('/job-list.html')
def job_list():
    return render_template('job-list.html')

@app.route('/testimonial.html')
def testimonial():
    return render_template('testimonial.html')

@app.route('/category.html')
def category():
    return render_template('category.html')

@app.route('/404.html')
def error():
    return render_template('404.html')

@app.route('/register.html')
def register():
    return render_template('register.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
