#!/usr/bin/env python3
"""A module to use the gettext of babel"""

from flask_babel import gettext, init_app
babel = __import__('2-app').babel


home_title = gettext(u"Welcome to Holberton")
home_header = gettext(u'Hello world!')

if __name__ == '__main__':
    init_app(babel)