import mysql.connector
from flask import Flask

app = Flask(__name__)

def connect_to_database():
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_HOST'] = 'localhost' 
    app.config['MYSQL_DB'] = 'petify'

    try:
        # Încercăm să stabilim conexiunea
        conn = mysql.connector.connect(
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            host=app.config['MYSQL_HOST'],
            database=app.config['MYSQL_DB']
        )
        cursor = conn.cursor()
        # Dacă conexiunea a fost stabilită cu succes, afișăm un mesaj
        print("Conexiune la baza de date reușită!")
        return conn, cursor

    except mysql.connector.Error as e:
        # În caz de eroare, afișăm un mesaj de eroare și gestionăm excepția
        print("Eroare la conectarea la baza de date:", e)

        # Închidem conexiunea în caz de eroare
        if 'conn' in locals():
            conn.close()
        return None, None