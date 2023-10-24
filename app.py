
import os
from flask import Flask , render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('redirectToThisFunction'))

@app.route('/upload/')
def redirectToThisFunction():
    return render_template('upload.html')

"""
redirect and url_for:

1. import redirect and url_for from flask module
2. call redirect and url_for (line 9)
"""