#!/usr/bin/python3
''' Starts a Flask web app '''
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    '''Renders the cities in a state '''
    states = list(storage.all(State).values())

    states.sort(key=lambda x: x.name)

    _list = []
    for state in states:
        state_cities = (state, sorted(state.cities, key=lambda x: x.name))
        _list.append(state_cities)
    return render_template('8-cities_by_states.html', s_c=_list[1:])


@app.teardown_appcontext
def teardown(error):
    ''' Clean up method '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
