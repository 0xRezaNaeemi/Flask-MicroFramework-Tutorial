from flask import Flask , render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit/', methods=["POST"]) # methods=["POST", "GET"]
def showResult():
    email = request.form['email']
    # email = request.form.get('email', 'no email')
    password = request.form['password']
    return render_template('result.html', email=email, password=password)
"""
1. work with form
2. send data with POST method
"""

