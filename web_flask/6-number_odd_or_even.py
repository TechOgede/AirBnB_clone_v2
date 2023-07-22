#!/usr/bin/python3
'''Starts a Flask web application'''

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    ''' Returns Hello HBNB'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' Returns HBNB '''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    ''' Returns custom text '''
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def Python(text='is cool'):
    ''' Returns custom text '''
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    ''' Returns custom text containing integer '''
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    ''' Renders a HTML page '''
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd_template(n):
    ''' Renders a HTML page '''
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
