
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Home page"


@app.route("/api")
def handleAPI():
    my_dictionary = {
        "Products":[
            {"name": "iphone", "price": 2588520, "stock": True},
            {"name": "samsung", "price": 25884520, "stock": False},
            {"name": "huawei", "price": 258520, "stock": True},
            {"name": "realme", "price": 15487514, "stock": False},
        ]
    }
        
    return my_dictionary

