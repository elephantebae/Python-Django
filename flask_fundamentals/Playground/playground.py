from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template("index.html")

@app.route('/play/<num>')
def makebox(num):
    return render_template("index.html", num = int(num))

@app.route('/play/<num>/<color>')
def makeboxeswithcolor(num, color):
    return render_template("index.html", num = int(num), color = color)













if __name__=="__main__":
    app.run(debug=True)