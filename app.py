
import os
from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route('/')
def home():
    if request.cookies.get("user_email"):
        return f"welcome your email is: {request.cookies['user_email']}"
    else:
        return render_template('form.html')


@app.route("/submit", methods=["POST"])
def submitForm():
    try:
        email = request.form["email"]
        # password = request.form["password"]

        # request.cookies["email"] = "asdf" # this dic is immuteable 
        # 
        response = make_response("Successful <a href='/'> HOME </a>")
        response.set_cookie("user_email", email)
        return response
    except Exception as e:
        return f"sorry not successful the error was: {e}"


"""
cookies:

1.import request, make_response 
2. no need to import cookies because cookies are in request
2. we can not use request.cookies["email"] = "asdf" because Dictionary is imuteable
3.  make_response convert returned responses to client, so we can add cookies to responses by make_response function
4. create "if" statement in home def for checking cookies
"""
