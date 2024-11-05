#!/usr/bin/env python3
"""A mnodule to instantiate using Babel"""

from flask_babel import Babel
from flask import Flask

app = Flask(__name__)
babel = Babel(app)


class Config:
    """A config class to store languages and other"""

    LANGUAGES = ["en", "fr"]

    @babel.localeselector
    def locale(self):
        """To set the babel local language"""

        return self.LANGUAGES[0]

    @babel.timezoneselector
    def timezone():
        """To set the time zone"""

        return 'UTC'


# app.config.from_object('Config')

config = Config()

config.locale()
