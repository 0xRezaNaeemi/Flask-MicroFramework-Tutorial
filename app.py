from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name="Reza")

"""
1. put 'name="Reza"' in render_template function as a second argument
2. use '{{name}}' variable in index.html
"""

