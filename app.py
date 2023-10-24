
import os
from flask import Flask , render_template, request

path = os.path.join("uploads")

os.makedirs(path, exist_ok=True)

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
    if theFile.filename != "":
        try:
            goal_path = theFile.save(os.path.join(path, theFile.filename))
            theFile.save(goal_path)
            return "your file has been saved successfully"
        except Exception as e:
            return e
    else:
        return "the file name is invalid"


