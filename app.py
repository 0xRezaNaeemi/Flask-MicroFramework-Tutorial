
import os
from flask import Flask , render_template, request

path = os.path.join("uploads")

os.makedirs(path, exist_ok=True)

app = Flask(__name__)

allowed_formats = {"txt", "jpg", "png"}
def checkFileFormat(fileName):
    return "." in fileName and fileName.rsplit(".", 1)[1] in allowed_formats

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

    if checkFileFormat(theFile.filename):
        try:
            goal_path = os.path.join(path, theFile.filename)
            theFile.save(goal_path)
            return "your file has been saved successfully."
        except Exception:
            return "oh! something is wrong."
    else:
        return "Your file format is not allowed."



"""
File format filter in front-end:

1. recode upload.html (line 89), 
    Use the accept attribute of the input tag.
    To accept only PNG's, JPEG's and GIF's you can use the following code:
    <input type="file" accept="image/png, image/gif, image/jpeg" name="file"/>
"""