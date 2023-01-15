#!/usr/bin/python3
"""Start a flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strick_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNBi!."""
    return "Hello HBNB!"


@app.route("/hbnb", striick_slahes=False)
def hbnb():
    """Displays 'HBNB'."""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
