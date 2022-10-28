from flask import Flask, render_template, request
from DbContext import create_connection
from controller import GpxController

# index.html <- controller.py <- app.py
#                   V
#                model.py -> DbContext.py

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return GpxController.index
