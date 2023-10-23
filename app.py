from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    context = [1, 2, 3, 4, 5]
    return render_template('index.html', my_list=context)

@app.route('/<name>/')
def welcome(name):
    return render_template('welcome.html', name=name)

"""
1. pass name variable from url to templates
2. use name in index.html
"""

