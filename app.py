
from flask import Flask
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
    return db_dir

"""
create database:

1. pip install Flask-SQLAlchemy 
2. from flask_sqlalchemy import SQLAlchemy
3. app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_dir
4. creating a database use this function
    with app.app_context():
        db.create_all()

"""