from pickle import APPEND
from flask import request,redirect
from flask import render_template
import model
import folium
import Gpx

class GpxController():

    def index():
        (fahrerList, status) = model.Fahrer.getFahrer()    
        return render_template('index.html', fahrerList = fahrerList)

    def fahrzeug(fid, fahrername):
        (fzids, status) = model.Fahrzeug.getFahrzeugIds(fid)
        (fahrzeugList) = model.Fahrzeug.getFahrzeug(fzids)
        return render_template('fahrzeug.html', fahrerList = fahrername, fahrzeugList = fahrzeugList)

    def fahrt(fid, fzid, startDate, endDate, fahrername, fahrzeugList):
        fahrtenList = []
        fahrtenEmpty = False
        #Alle fahrten die der Fahrer mit dem Fahrzeug gefahren ist
        (fahrtenGes, status) = model.Fahrt.getFahrt(fid, fzid)
        #Alle fahrten die der fahrer zwischen startDate und endDate gefahren ist
        (fahrten, status) = model.Fahrt.getFahrtenBetweenDates(startDate, endDate)
        for f in fahrten:
            for fa in fahrtenGes:
                if fa[0] == f:                   
                    if len(fahrtenList) > 0:
                        for x in fahrtenList:
                            if x[0] != fa[0]:
                                fahrtenList.append(fa)
                                break
                    else:
                        fahrtenList.append(fa)

        if len(fahrtenList) < 1:
            fahrtenList.append("")
            fahrtenEmpty = True

        print(fahrtenList)
        return render_template('fahrt.html', fahrerList = fahrername, fahrzeugList = fahrzeugList, fahrtenList = fahrtenList, fahrtenEmpty = fahrtenEmpty)

    def map(ftid):
        (points, status) = model.Fahrtpunte.getPoints(ftid)
        map = Gpx.overlayGPX(points, 14)
        folium_map = map
        return folium_map._repr_html_()


def main():
    # GpxController.map('2')
    #GpxController.fahrt('3','8','1900-01-01', '2022-12-30', 'faffa', 'fafa')
    GpxController.map('12')

if __name__ == '__main__':
    main()