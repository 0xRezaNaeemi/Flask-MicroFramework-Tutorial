
import os
from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/404')
def error404():
    # abort(503)
    abort(404)

@app.errorhandler(404)
def showError(error):
    # return "The error is " + str(error)
    return render_template("404.html"), 404


"""
error 404 handling:

1. import abort from flask module
2. use abort (line 16-24)
3. create 404.html
4. type mispelled route in url 
    http://127.0.0.1:5000/formm
"""
