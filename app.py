from contextlib import redirect_stderr, redirect_stdout
from flask import Flask, render_template, request
from DbContext import create_connection
from controller import GpxController

# index.html <- controller.py <- app.py
#                   V
#                model.py -> DbContext.py

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
<<<<<<< HEAD
@app.route("/home")
def hello():
    return render_template("home.html")

=======
def home():
    return GpxController.index
>>>>>>> 2e467b8178cc541986612fa666a4b031a77adcef
