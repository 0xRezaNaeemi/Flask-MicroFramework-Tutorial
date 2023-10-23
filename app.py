from flask import Flask , render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit/')
def showResult():
    # email = request.args['email']
    email = request.args.get('email', 'no email')
    password = request.args['password']
    return render_template('result.html', email=email, password=password)
"""
1. work with form
2. send data with GET method from to urls 
"""

