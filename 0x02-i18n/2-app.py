#!/usr/bin/env python3
"""A module to create an app using flask"""

from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)


class Config:
    """A config class to store languages and other"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector()
def get_locale():
    """To get the best language match"""

    request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def get_home():
    """The home page"""

    return render_template('2-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
