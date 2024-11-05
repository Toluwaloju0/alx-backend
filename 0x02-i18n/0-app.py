#!/usr/bin/env python3
"""A module to create an app using flask"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def get_home():
    """The home page"""

    return render_template('0-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
