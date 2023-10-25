
from datetime import timedelta
from flask import Flask, render_template, request, make_response, session

app = Flask(__name__)

app.secret_key = "aaaaaaadasdasfsadfsdafsdfsda"
app.permanent_session_lifetime = timedelta(days=1)



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
        session.permanent = True
    
        
        return "Successful <a href='/'> HOME </a>"
    except Exception as e:
        return f"sorry not successful the error was: {e}"


"""
session expired date:

1. from datetime import timedelta
2. session.permanent = True
3. app.permanent_session_lifetime = timedelta(days=1)

"""
