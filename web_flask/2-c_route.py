#!/usr/bin/python3
"""Starts a Flask web application.

The application listons on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays "C" followed by the value of <text>.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strick_slashes=False)
def hello_hbnb():
    """Displays "Hello HBNB!."""
    return 'Hello HBNB!'

@app.route("/hbnb", strick_slashes=False)
def hello_hbnb():
    """Dislays 'Hello HBNB!'"""
    return "HBNB"

@app.route('/c/<text>', followed by the value of <text>
        def c(text):
        """Displays "C" followed by the value of <text>."""
        text = text.replace("_", " ")
        return "C {}".format(text)

if __name__ == "__main__":
app.run(host='0.0.0.0', port=5000)
