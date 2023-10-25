
import os
from flask import Flask, render_template, abort, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/admin')
def adminPanel():
    # abort(503)
    # abort(404)
    # abort(redirect(url_for('index')))
    abort(redirect("404.html"))

@app.errorhandler(404)
def showError(error):
    # return "The error is " + str(error)
    return render_template("404.html"), 404


"""
abort function:

1.import abort, redirect, url_for functions
2. create admin route
3. for security purpose we abort 404 or redirect to home  
    http://127.0.0.1:5000/admin
"""
