from flask import Flask, render_template, request

from triangle import Triangle

app = Flask(__name__)

@app.route("/",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/",methods=['POST'])
def calc():
    try:
        trtr =  request.form.get('trtr')
        a,b,c = map(float, trtr.split(' '))
        t = Triangle(a, b, c)
        return render_template('index.html', p=t.perimeter(), s=t.area())
    except Exception as err:
        return render_template('index.html', error_msg = str(err) )
if __name__ == "__main__":
    app.run(host='0.0.0.0')