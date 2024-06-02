#!/usr/bin/python3
""" A script that says Hello BNB
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hnb', strict_slashes=False)
def hbnb():
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
