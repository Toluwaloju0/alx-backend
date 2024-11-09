#!/usr/bin/env python3


from flask import render_template
app = __import__('2-app').app

@app.route('/3')
def get_3():
    return render_template('3-index.html')
