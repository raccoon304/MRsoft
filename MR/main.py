from importlib.resources import contents
from flask import Flask, render_template, request, redirect, url_for
import sys, json, pyrebase

with open("./auth/auth.json") as f:
    config = json.load(f)
    

firebase = pyrebase.initialize_app(config)
db = firebase.database()


login_conf = {"id":"smon0376", "password":"ths58975897!","username":"raccoon"}
db.child("users").child("abcd").set(login_conf)


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test/")
def test():
    return render_template("test.html")
if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug=True)
