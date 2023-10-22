from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

"""
1. create 'templates' folder
2. create index.html in templates folder
3. import render_template function from flask module
4. create home route and return render_template('index.html')
"""

