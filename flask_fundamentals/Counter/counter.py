from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'helasodasd'
@app.route('/')
def howmany():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 0
    return render_template("index.html", count = session['counter'])
@app.route('/addtwo')
def addtwo():
    if 'counter' in session:
        session['counter'] += 1
    return redirect('/')
@app.route('/destroy_session')
def destroysession():
    if session:
        session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
