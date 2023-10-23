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
Bugs: in welcome page style.css does not load successfully
1. (Optional): move static/style.css to static/css/style.css
2. use 'url_for' in templates for linking style.css
    {{url_for('static', filename='css/style.css')}}
"""

