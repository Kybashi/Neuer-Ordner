from flask import Flask, render_template, request
from DbContext import create_connection

database = r"C:\DB\gpx\gpx.db"

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    conn = create_connection(database)
    fahrt = ('testname',1,2)

    return "Hello, Flask!"
