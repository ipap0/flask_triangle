import sqlite3

def get_connection():
       connection = sqlite3.connect('triangles.db')
       return connection

def init_db():
    connection = get_connection()
    cursor = connection.cursor()

    # Создаем таблицу Users
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Triangles (
    id INTEGER PRIMARY KEY autoincrement,
    a INTEGER NOT NULL,
    b INTEGER NOT NULL,
    c INTEGER NOT NULL
    )
    ''')

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()