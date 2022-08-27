from flask import Flask, render_template, request, redirect
import sys
from importlib.resources import contents

app = Flask(__name__)

@app.route("/")
def home():
    return "Wg"


if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)

