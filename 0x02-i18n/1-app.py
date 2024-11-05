#!/usr/bin/env python3
"""A mnodule to instantiate using Babel"""

from flask_babel import Babel

app = __import__('0-app').app


class Config:
    """A config class to store languages and other"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)
