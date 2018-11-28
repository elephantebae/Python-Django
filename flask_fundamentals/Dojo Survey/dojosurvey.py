from flask import Flask, render_template, request, redirect,session, flash
from mysqlconnection import connectToMySQL
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=["POST"])
def resultsofform():
    name_from_form = request.form["yourname"]
    dojo_from_form = request.form["dojolocation"]
    favorite_from_form= request.form["favlocation"]
    comment_from_form= request.form["comment"]
    
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)

   
