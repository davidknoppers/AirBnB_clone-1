#!/usr/bin/python3
"""
Script that starts a basic Flask web app
With our databases accessible from the backend
Further scripts will make the website more sophisticated
"""
from models import storage

from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def closing_time(self):
    """
    The SQLAlchemy session doesn't have to go home, but it can't stay here
    """
    storage.close()


@app.route('/states_list/')
def states_list():
    """
    list all states from storage
    """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
