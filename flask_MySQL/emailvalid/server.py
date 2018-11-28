from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import connectToMySQL
import re
app = Flask(__name__)
app.secret_key = "aasdfas"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    if not EMAIL_REGEX.match(request.form['email']):    # test whether a field matches the pattern
        flash("Invalid email address!")
        return redirect('/')
    else:
        flash("The email address you entered " + request.form['email'] + "is a VALID email adress! Thank you!")
        mysql = connectToMySQL("email")
        query= "INSERT INTO email(email) VALUES (%(em)s);"
        data ={
            'em': request.form['email']
        }
        mysql.query_db(query, data)
        return redirect('/processed')

@app.route('/processed')
def processed():
    mysql = connectToMySQL("email")
    pull = mysql.query_db("SELECT * FROM email")
    return render_template("processed.html", e_return = pull)
if __name__ == "__main__":
    app.run(debug=True)