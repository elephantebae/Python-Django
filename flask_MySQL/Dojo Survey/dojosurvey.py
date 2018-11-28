from flask import Flask, render_template, request, redirect,session, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)
app.secret_key = "asdfasdaf"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/storedresult', methods=["POST"])
def storeandredirect():
    is_valid= True
    if len(request.form['name'])< 1:
        is_valid = False
        flash("Please enter Name")
    if is_valid:
        mysql = connectToMySQL("survey")
        query = "INSERT INTO users(name, location, comment, favlang) VALUES (%(nm)s,%(d)s,%(c)s,%(l)s);" 
        data = {
            'nm': request.form["name"],
            'd': request.form["dlocation"],
            'l': request.form["lang"],
            'c': request.form["comment"],
        }
        mysql.query_db(query,data)
    return redirect('/result')
@app.route('/result')
def resultsofform():
    mysql = connectToMySQL("survey")
    allinfo =mysql.query_db("SELECT * FROM users")
    return render_template("result.html", usersinfo = allinfo)



if __name__ == "__main__":
    app.run(debug=True)

   
