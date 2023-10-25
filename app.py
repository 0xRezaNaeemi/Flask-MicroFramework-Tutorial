
import os
from flask import Flask, render_template, request, make_response, session

app = Flask(__name__)

app.secret_key = "aaaaaaadasdasfsadfsdafsdfsda"

@app.route('/')
def home():
    if session.get("user_email"):
        return f"welcome your email is: {session['user_email']}"
    else:
        return render_template('form.html')


@app.route("/submit", methods=["POST"])
def submitForm():
    try:
        email = request.form["email"]
        # password = request.form["password"]
         
        session["user_email"] = email
        return "Successful <a href='/'> HOME </a>"
    except Exception as e:
        return f"sorry not successful the error was: {e}"


"""
cookies:

1.import session
2. add secret_key for app (line 7)
2. recode cookies to session 

"""
