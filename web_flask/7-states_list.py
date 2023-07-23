#!/usr/bin/python3
''' Starts a flask app '''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    ''' Renders template to display list of states '''
    states = list(storage.all(State).values())

    states.sort(key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tear_down(error):
    ''' Removes current SQLALchemy Sessioon '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
