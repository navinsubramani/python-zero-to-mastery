# Run using command: flask --app 019_Web_Development/268 --debug run

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/<string:htmlpages>")
def subpages(htmlpages=None):
    return render_template(htmlpages)