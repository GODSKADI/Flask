from flask import Flask, request
app = Flask(__name__)

from random import randint

num = randint(0,100)

@app.route('/')
def inicio():
    return str(num) + """<form action='result' method='post'>
    <h1>Adivina el Numero LOK@</h1>
    <h2>Introduce un numero</h2>
    <input type='number' name='num'></input>
    <input type='submit' value='Enviar'/>
    </form>"""

@app.route('/result', methods= ['POST'])
def result():
    error = None
    if request.method == 'POST':
        if request.form['num'] != str(num):
            return "Fallaste" + str(num)
        else:
            return "Eres Buenisimo"
