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

@app.route('/upload/')
def upload():
    return render_template('upload.html')

@app.route('/uploaded/', methods=['POST'])
def savefile():
    theFile = request.files['file']
    return theFile.filename



"""
1. upload a file
2. send data with POST method
"""

