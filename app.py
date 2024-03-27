from flask import Flask, render_template

app = Flask(__name__)

DEBUG = True

@app.route("/")
def home():
    return render_template("pages/home.html")

@app.route("/about")
def about():
    return render_template("pages/about.html")

@app.route("/services")
def services():
    return render_template("pages/services.html")

@app.route("/contact")
def contact():
    return render_template("pages/contact.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("pages/404.html")