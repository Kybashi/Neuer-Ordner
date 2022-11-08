import re
from flask import Flask, render_template, request
from DbContext import create_connection
from controller import GpxController

# index.html <- controller.py <- app.py
#                   V
#                model.py -> DbContext.py

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    print('home')
    print(request.method)
    return GpxController.index()

@app.route('/fahrzeug', methods=['GET', 'POST'])
def fahrzeug():
    print(request.form['fahrer'])
    print(request.method)
    fahrer = request.form['fahrer']
    global fid
    fid = fahrer[1]
    fahrerName = fahrer[5]
    return GpxController.fahrzeug(str(fid), str(fahrerName))

@app.route('/fahrt', methods=['GET', 'POST'])
def fahrt():
    print('fahrt')
    print(request.method)
    global fid
    global fzid
    fahrzeug = request.form['fahrzeug']
    id = re.split(",", fahrzeug)[0]#fahrzeug[1]
    fzid = id.replace('(','')
    fahrzeugname = fahrzeug[5:14]
    print(fahrzeug)
    print(fahrzeugname)
    print(fid)
    print(fzid)
    fahrtVon = request.form['datum_von']
    fartBis = request.form['datum_bis']
    fahrer = request.form['fahrer']
    return GpxController.fahrt(str(fid), str(fzid), fahrtVon, fartBis, fahrer, fahrzeugname)

@app.route('/map', methods=['GET', 'POST'])
def map():
    print('map')
    print(request.method)
    string = request.form['fahrt']
    id = re.split(",", string)[0]
    ftid = id.replace('(','')
    print(ftid)
    return GpxController.map(ftid)