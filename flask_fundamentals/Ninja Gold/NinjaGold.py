from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "asdfasdaf"

@app.route('/')
def index():
    if 'counter' in session:
        pass
    else:
        session['counter'] = 0
        session['howmuchgold'] = 0
    return render_template("index.html", gold = session['howmuchgold'])

@app.route('/process_money',methods=['POST'])
def processing():
    if request.form['building'] == 'farm':
        session['howmuchgold'] += random.randint(9,20)
    elif request.form['building'] == 'cave':
        session['howmuchgold'] += random.randint(4,10)
    elif request.form['building'] == 'house':
        session['howmuchgold'] += random.randint(1,6)
    elif request.form['building'] == 'casino':
        session['howmuchgold'] += random.randint(-51,51)
    return redirect('/', )


if __name__ == "__main__":
    app.run(debug = True)