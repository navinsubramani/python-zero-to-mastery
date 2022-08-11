# Run using command: flask --app 019_Web_Development/261 --debug run

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/blog")
def blog():
    return render_template('blog.html')


@app.route("/help")
def help():
    return "<p>TO BE UPDATED....</p>"


@app.route("/about/<username>")
def about(username=None):
    return render_template('about.html', name=username)
