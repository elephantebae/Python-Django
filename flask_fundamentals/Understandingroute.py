from flask import Flask, render_template
app = Flask(__name__)

print(__name__)
@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times =5)
def hello_world():
    return "hello world!"

@app.route('/dojo')
def sayDojo():
    return "Dojo!"

@app.route('/say/<name>')
def hello(name): 
    return "Hi " + name + "!"

@app.route('/repeat/<number>/<word>')
def repeatword(number,word):
        return int(number) * str(word) 
    



if __name__=="__main__":

        app.run(debug=True)
