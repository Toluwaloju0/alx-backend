#!/usr/bin/env python3
"""A module to set flask to use a requests locale"""

from flask import request
from typing import List
babel = __import__('1-app').babel
app = __import__('1-app').app

def get_locale() -> List[str]:
    """To get the besgt language match"""

    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel.locale_selector = get_locale()
