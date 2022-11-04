from flask import Flask, render_template, request
from DbContext import create_connection
from controller import GpxController

# index.html <- controller.py <- app.py
#                   V
#                model.py -> DbContext.py

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    t = request.form['fahrer']
    #the_date = request.form['date_von']
    print(t)
    #print(the_date)
    print(request.method)
    return GpxController.index()

