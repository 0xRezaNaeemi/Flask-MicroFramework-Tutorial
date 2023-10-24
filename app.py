
import os
from flask import Flask , render_template, request,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/upload")

@app.route('/upload/')
def upload():
    return render_template('upload.html')

"""
redirect function:

1. import redirect function from flask module
2. call redirect (line 9)
"""