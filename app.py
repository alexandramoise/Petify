from flask import Flask, render_template
from dbconnection import connect_to_database

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/db')
def check_db():
    conn, cursor = connect_to_database()
    if conn and cursor:
        cursor.close()
        conn.close()
        return render_template('something.html')
    else:
        return None


if __name__ == '__main__':
    app.run(debug=True)
