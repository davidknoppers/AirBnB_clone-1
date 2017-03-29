#!/usr/bin/python3
from models import storage
from console import HBNBCommand
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', defaults={'id': None})
@app.route('/states/<id>')
def states_html(id):
    """
    Returns ordered list of states with cities or Not Found
    """
    states = storage.all("State")
    if (id is None):
        return render_template('9-states.html', states=states, id='all_states')
    else:
        for val in states.values():
            if val.id == id:
                state = val
                return render_template('9-states.html',
                                       states=state, id='one_state')
        return render_template('9-states.html', states=states, id='none')


@app.teardown_appcontext
def teardown(self):
    """
    simply calls our close functions from storage
    """
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
