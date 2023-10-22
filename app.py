# import Flask class from flask modules
from flask import Flask 

# create app instance from Flask class
app = Flask(__name__)

# home page
@app.route('/')
def index():
    return "This is home/index page!"

# blog page
@app.route('/blog/')
def blog():
    return "welcome to flask journey!"

# using post_id variable in route
@app.route('/blog/<int:post_id>/')
def postId(post_id):
    return f"post id is: {post_id}"

# No need to write str variable type in route
@app.route('/welcome/<name>/')
def sayWelcome(name):
    return f"welcome: {name}"



"""
1. create a folder 
eg: 'test FLASK rad'

2. open folder with code editor 
eg: 'VS code'

3. create Virtual Envirement from VSCODE terminal 
eg: -->python -m venv venv

4. activate venv from vscode terminal 
eg: -->venv\Scripts\activate

5. install Flask Framework 
eg: -->python -m pip install flask

6. create requirements.txt 
eg: -->pip freeze > requirements.txt

7. create a python file named app.py and start coding...

8. set app.py to flask envirements variables 
eg: -->set FLASK_APP=app.py

9. run flask server
eg: -->run flask

10. go to http://127.0.0.1:5000 in browser

11. Yay! Welcome to Web World...
"""