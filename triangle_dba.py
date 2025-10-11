from db_connect import get_connection
from triangle import Triangle


def get_triangles():
    triangles = []
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Triangles')
    triangle_tuples = cursor.fetchall()
    for tuple in triangle_tuples:
        t = Triangle(tuple[1], tuple[2], tuple[3])
        triangles.append(t)
    return triangles

def save_triangle(tr):
    con = get_connection()
    cursor = con.cursor()
    cursor.execute('INSERT INTO Triangles (a, b, c) VALUES (?, ?, ?)', (tr.a, tr.b, tr.c))
    con.commit()
    con.close()

