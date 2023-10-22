from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

"""
1. create 'static' folder
2. create style.css in static folder
3. link style.css with index.html
4. change body background-color in style.css
"""

