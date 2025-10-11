#import sqlite3
import psycopg2

def get_connection():
       #connection = sqlite3.connect('triangles.db')
       connection = psycopg2.connect(
           dbname="geometry",
           user="postgres",
           password="123",
           host="10.10.105.107",
           port="5432"
       )
       return connection

def init_db():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
     CREATE TABLE IF NOT EXISTS Triangles (
          id INTEGER PRIMARY KEY generated always as identity not null,
          a float NOT NULL,
          b float NOT NULL,
          c float NOT NULL
          )
     ''')

    connection.commit()
    connection.close()