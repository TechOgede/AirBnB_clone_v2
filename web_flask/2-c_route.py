#!/usr/bin/python3
'''Starts a Flask web application'''

from flask import Flask
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
