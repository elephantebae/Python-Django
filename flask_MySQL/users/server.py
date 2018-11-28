from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route("/users/new/")
def makeaction():
    return render_template("index.html", action = "new")

@app.route("/users/create/", methods=["POST"])
def newuser():
    mysql = connectToMySQL("users")
    query = "INSERT INTO userslist(first_name, last_name, email, created_at, updated_at) VALUES (%(fn)s,%(ln)s, %(em)s, NOW(),NOW());"
    data = {
        'fn': request.form["firstname"],
        'ln': request.form["lastname"],
        'em': request.form["email"],
    }
    new_user=mysql.query_db(query,data)
    return redirect(f"/users/{new_user}/")
    

@app.route("/users/<new_user>/")
def madeuser(new_user):
    mysql = connectToMySQL("users")
    data = {
        'id': new_user
    }
    thisuser = mysql.query_db("SELECT * FROM userslist WHERE id = %(id)s;", data)
    return render_template("index.html", action = "users", c_user = thisuser)


@app.route("/users/<new_user>/edit/")
def holdeditpage(new_user):
    mysql = connectToMySQL("users")
    data = {
        'id': new_user
    }
    edituser = mysql.query_db("SELECT * FROM userslist WHERE id = %(id)s;" ,data)
    return render_template("index.html", action = "editusers", e_user= edituser)

@app.route("/users/<new_user>/edited", methods=['post'])
def edit(new_user):
    mysql = connectToMySQL("users")
    query = "UPDATE userslist SET first_name = %(fn)s, last_name = %(ln)s, email = %(em)s WHERE id = %(id)s;"
    data = {
        'fn': request.form['fname'],
        'ln': request.form['lname'],
        'em': request.form['mail'],
        'id': new_user
    }
    mysql.query_db(query,data)
    return redirect("/users")

@app.route("/users")
def tableusers():
    mysql = connectToMySQL("users")
    allusers = mysql.query_db("SELECT * FROM userslist")
    return render_template("index.html", action = "allusers", ausers= allusers)

@app.route("/users/destroy/<id>")
def destroy(id):
    mysql = connectToMySQL("users")
    data = {
        'id': id
    }
    mysql.query_db("DELETE FROM userslist WHERE id = %(id)s;",data)
    return redirect("/users")

if __name__ == "__main__":
    app.run(debug=True)