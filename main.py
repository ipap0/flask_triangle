from flask import Flask, render_template, request

from triangle import Triangle, TrException

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/", methods=['POST'])
def calc():
    try:
        a = float(request.form.get('a'))
        b = float(request.form.get('b'))
        c = float(request.form.get('c'))
        # a,b,c = map(float, trtr.split(' '))
        t = Triangle(a, b, c)
        return render_template('index.html', p=round(t.perimeter(),3), s=round(t.area(), 3), a=a, b=b, c=c)
    except TrException as err:
        return render_template('index.html', error_msg=str(err))
    except Exception as err:
        return render_template('index.html', error_msg='не удалось преобразовать ваши исходные данные')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
