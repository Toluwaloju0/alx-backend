#!/usr/bin/env python3
"""A module to force a locale on a web page"""

from flask import request
from flask_babel import force_locale
app = __import__('3-app').app
get_locale = __import__('2-app').get_locale

locale = get_locale()

if locale == 'fr':
    with force_locale(locale):
        return render_template('4-index.html')
