from flask import Flask, render_template

app = Flask(__name__)

DEBUG = True

@app.route("/")
def home():
    return render_template("pages/home.html")