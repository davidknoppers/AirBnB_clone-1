#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """
    simple hello world-type fn
    """
    return ('Hello HBNB!')


@app.route('/hbnb')
def just_hbnb():
    """
    simple hello world-type fn
    """
    return ('HBNB')


@app.route('/c/<text>')
def c_route(text):
    """
    returns C +  _-> spaces
    """
    return ("C "+text.replace("_", " "))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
