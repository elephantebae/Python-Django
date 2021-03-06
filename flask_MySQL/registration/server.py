from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
import re
from flask_bcrypt import Bcrypt        
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "asdfasd"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/registerprocess', methods=["POST"])
def process():
    is_valid = True
    if len(request.form['fname']) < 1:
        is_valid = False
        flash("You must input first name!", "firstname")
        
    if len(request.form['lname']) < 1:
        is_valid = False
        flash("You must input last name!", "lastname")

    if not EMAIL_REGEX.match(request.form['email']):    # test whether a field matches the pattern
        flash("Invalid email address!", "email")

    mysql = connectToMySQL("register")
    query ="SELECT * FROM user WHERE email = %(em)s"
    data = {
        'em' : request.form['email']
    }
    checkdupemail = mysql.query_db(query,data)
    print(checkdupemail)
    if checkdupemail:
        is_valid = False
        flash("email is already in use!", "dupemail")
    
    if len(request.form['password']) < 8:
        is_valid = False
        flash("Your password must be longer than 8 Characters","pw")
    
    if request.form['cpassword'] != request.form['password']:
        is_valid = False
        flash("Your password must be matching!","cpw")
    
    if is_valid == False:
        return redirect('/')
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['password']) 
        mysql = connectToMySQL("register")
        query = "INSERT INTO user(first_name,last_name,email,password) VALUES(%(fn)s, %(ln)s, %(em)s, %(password_hash)s);"
        data = {
            'fn': request.form['fname'],
            'ln': request.form['lname'],
            'em': request.form['email'],
            "password_hash" : pw_hash
        }
        mysql.query_db(query,data)
        # also save user id in session
        session['user'] = request.form['fname']
        return redirect("/success")
@app.route("/success")
def youmadeit():
    return render_template("success.html", winnerwinner = session['user'] )

@app.route("/loginprocess", methods=["POST"])
def loginprocess():
    mysql = connectToMySQL("register")
    query = "SELECT * FROM user WHERE email = %(email)s;"
    data = {"email" : request.form["email"]}
    result = mysql.query_db(query,data)
    if result: 
        if bcrypt.check_password_hash(result[0]['password'], request.form['lpassword']):
            session['useremail'] = result[0]['email']
            session['user'] = result[0]['first_name']
        return redirect("/success")
        
    else:
        flash("Did not work", "errorlogin")
        return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)
