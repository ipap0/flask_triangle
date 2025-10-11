from flask import Flask, render_template, request

from db_connect import init_db
from triangle import Triangle, TrException
from triangle_dba import save_triangle, get_triangles

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    init_db()
    return render_template('index.html')


@app.route("/", methods=['POST'])
def calc():
    try:
        a = float(request.form.get('a'))
        b = float(request.form.get('b'))
        c = float(request.form.get('c'))
        # a,b,c = map(float, trtr.split(' '))
        t = Triangle(a, b, c)
        save_triangle(t)
        return render_template('index.html', p=round(t.perimeter(),3), s=round(t.area(), 3), a=a, b=b, c=c)
    except TrException as err:
        return render_template('index.html', error_msg=str(err))
    except Exception as err:
        #return render_template('index.html', error_msg='не удалось преобразовать ваши исходные данные')
        return render_template('index.html', error_msg=str(err))

@app.route("/list", methods=['GET'])
def list():
    triangles = get_triangles()
    return render_template('list.html', triangles=triangles)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
