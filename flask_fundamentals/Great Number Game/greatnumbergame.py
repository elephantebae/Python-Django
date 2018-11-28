from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key ="bop bop bop"

@app.route('/')
def index():
    if 'counter' in session:
        pass
    else:
        session['counter'] = 0
        session['savethenumber'] =random.randint(1, 101)
        session['reply'] = int()
    return render_template("index.html", answer = int(session['savethenumber']),
    player1answer = int(session['reply']))

@app.route('/results', methods=["POST"])
def returnedanswers():
    session['reply'] = request.form["guessnumber"]
    print (session['reply'])
    return redirect('/')
if __name__ =="__main__":
    app.run(debug=True)