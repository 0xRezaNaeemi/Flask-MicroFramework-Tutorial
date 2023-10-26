
from flask import Flask, session, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

path = os.path.dirname(__file__)
db_dir = os.path.join(path, "app.db")


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_dir

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

# use one time when creating a database
# with app.app_context():
#     db.create_all()

@app.route('/')
def home():
    users = User.query.all()
    # users2 = User.query.first()

    return render_template("result.html", users=users)

@app.route('/add')
def addUser():
    try:
        user = User()
        user.name = "Reza"
        db.session.add(user)
        db.session.commit()
        return "Adding user successfully!"
    except Exception as e:
        return "Adding user failed! error is: " + str(e)

"""
read from database

"""