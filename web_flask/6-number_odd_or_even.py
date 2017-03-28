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
    Returns C + string
    """
    return ("C "+text.replace("_", " "))


@app.route('/python/')
@app.route('/python/<text>')
def python_route(text="is cool"):
    """
    Returns Python + string
    """
    return ("Python "+text.replace("_", " "))


@app.route('/number/')
@app.route('/number/<int:n>')
def number_route(n):
    """
    prints if n is an int
    """
    return ("{} is a number".format(n))


@app.route('/number_template/')
@app.route('/number_template/<int:n>')
def number_template(n):
    """
    renders a basic HTML template
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/')
@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """
    returns basic string depending on an int being odd or even
    """
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
