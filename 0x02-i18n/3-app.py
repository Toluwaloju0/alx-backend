#!/usr/bin/env python3
from flask import render_template
app = __import__('2-app').app
babel = __import__('2-app').babel

@app.route('/')
def get_3():
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run()
