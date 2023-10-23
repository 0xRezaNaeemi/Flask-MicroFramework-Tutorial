from flask import Flask , render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    data = request.args["id"]
    return render_template('index.html', data=data)

"""
1. type in url 'http://127.0.0.1:5000/?id=12345'
2. request function get this dictionary and send to templates
"""

