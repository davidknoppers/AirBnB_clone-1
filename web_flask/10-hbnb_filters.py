#!/usr/bin/python3
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb_filters')
def filter_display():
    """
    sends lists of all states and amenities to be rendered
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)

@app.teardown_appcontext
def teardown(self):
    """
    simply calls our new close function
    """
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
