from pickle import APPEND
from flask import request,redirect
from flask import render_template
import model

class GpxController():

    def index():
        list = []
        (fahrerList, status) = model.Fahrer.getFahrer()

        (fahrzeugList, status) = model.Fahrzeug.getFahrzeug()
        
        return render_template('index.html', fahrerList = fahrerList, fahrzeugList = fahrzeugList)


if __name__ == '__main__':
    GpxController.index()