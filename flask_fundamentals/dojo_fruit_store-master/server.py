from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")



@app.route('/checkout', methods=['POST'])         
def process():
    qstrawberries = request.form['strawberry']
    qraspberries = request.form['raspberry']
    qapples= request.form['apple']
    fname = request.form['first_name']
    lname = request.form['last_name']
    maile= request.form['student_id']
    count = (int(qstrawberries)+ int(qapples) +int(qraspberries))
    print(f"Charging" +" "+ fname +" " +lname + " " + "for " + str(count) +" "+ "fruits")
    return render_template("checkout.html",
    quantitys = qstrawberries, quantityr= qraspberries,
    quantitya = qapples, first = fname, last = lname, mail = maile)



@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    