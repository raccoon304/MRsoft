from importlib.resources import contents
from flask import Flask, render_template, request, redirect, url_for
from DB_handler import DBModule
import sys, json, pyrebase

DB = DBModule
app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login/")
def login():
    return render_template("test.html")

@app.route("/login_done/")
def login_done():
    return render_template("test.html")


@app.route("/test2/<int:pid>")
def test2(pid):
    pass

@app.route("/signin/")
def signin():
    return render_template("signin.html")

@app.route("/signin_done/")
def signin_done():
    return render_template("base.html")

@app.route("/user/<uid>")
def user(uid):
    pass


if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug=True)
