#!/usr/bin/env python3
"""A module to force a locale on a web page"""

from flask import request, Flask, render_template
from flask_babel import force_locale
get_locale = __import__('2-app').get_locale
babel = __import__('3-app').babel

app = Flask(__name__)

@app.route('/')
def home():
    """The home page for 4-app"""

    force_locale('fr')
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
    
