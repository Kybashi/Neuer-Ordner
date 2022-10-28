from contextlib import redirect_stderr, redirect_stdout
from flask import Flask, render_template, request
from DbContext import create_connection

database = r"C:\DB\gpx\gpx.db"

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
@app.route("/home")
def hello():
    return render_template("home.html")

