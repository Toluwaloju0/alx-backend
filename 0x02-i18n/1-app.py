#!/usr/bin/env python3
"""A mnodule to instantiate using Babel"""

app = __import__('0-app').app
from flask_babel import Babel

babel = Babel(app)


class Config:
    """A config class to store languages and other"""

    LANGUAGES = ["en", "fr"]

    @babel.localeselector
    def locale():
        """To set the babel local language"""

        return config.LANGUAGES[0]

    @babel.timezoneselector
    def timezone():
        """To set the time zone"""

        return 'UTC'

app.config.from_object('Config')