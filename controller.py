from flask import request,redirect
from flask import render_template
import model

class GpxController():

    def index():
        fahrerList = model.Fahrer.getFahrer()
        fahrzeuge = model.Fahrzeug.getFahrzeug()
        
        return render_template('index.html', fahrerList = fahrerList)
