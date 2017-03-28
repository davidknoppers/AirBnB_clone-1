#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_hbnb():
    return ('Hello HBNB!')
@app.route('/hbnb')
def just_hbnb():
    return ('HBNB')
@app.route('/c/<text>')
def c_route(text):
    return ("C "+text.replace("_"," "))
@app.route('/python/')
@app.route('/python/<text>')
def python_route(text="is cool"):
    return ("Python "+text.replace("_"," "))
@app.route('/number/')
@app.route('/number/<n>')
def number_route(n):
    if int(n):
        return ("{} is a number".format(n))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
