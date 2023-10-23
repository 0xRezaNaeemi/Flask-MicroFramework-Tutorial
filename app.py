from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    context = [1, 2, 3, 4, 5]
    return render_template('index.html', my_list=context)

"""
1. create a list and pass to render_template
2. use 'for' from jinja templates language in index.html
"""

