from datetime import datetime
from http.client import OK
import gpxpy
import gpxpy.gpx
import os
import DbContext
import folium 

database = r"C:\DB\gpx\gpx.db"

def loopGpxfiles(gpxDir):
    for filename in os.listdir(gpxDir):
        gpx_file = open(gpxDir + '/' + filename, 'r')
        loopFile(gpx_file, filename)
    print("---END--")  
    return OK

def loopFile(file, filename):
    print("reading " + filename)
    gpx = gpxpy.parse(file)
    print("checking and inserting Data from " + filename + " to DB")
    (name, vorname, polkz) = parseFileName(filename)
    (fid, statusMessage) = checkfahrer(name, vorname)
    (fzid, statusMessage) = checkFahrzeug(polkz)
    (ftid, statusMessage) = checkFahrt(filename, fid, fzid)
    (pid) = checkFahrtpunkte(ftid, gpx)

def getFahrtpunkte(gpx):
    points = []
    try:
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    points.append(point)

        return points, "succeeded to get the track points"
    except:
        return points, "failed to get the track points"

def checkFahrtpunkte(ftid, gpx):   
    pointiDs = []
    (points, statusMessage) = getFahrtpunkte(gpx)

    for point in points:
        if not isinstance(point.elevation, float):
            point.elevation = ""

        if not isinstance(point.time,datetime):
            point.time = ""
        
        fahrtpunkt = (point.latitude, point.longitude, point.elevation, point.time, ftid)
        conn = DbContext.create_connection(database)
        (pid, message) = DbContext.select_fahrtpunktId(conn, fahrtpunkt)
        if message == False:
            pid = DbContext.create_fahrtpunkt(conn, fahrtpunkt)
            pointiDs.append(pid)
        else:
            pointiDs.append(pid)

    return pointiDs

def checkFahrt(filename, fid, fzid):
    fahrt = (filename, fid, fzid)
    conn = DbContext.create_connection(database)
    (ftid, message) = DbContext.select_fahrtId(conn, fahrt)
    if message == False:
        ftid = DbContext.create_fahrt(conn, fahrt)
        return ftid, "Fahrt created"
    else:
        return ftid, "Fahrt allready exists"

def checkfahrer(name, vorname):
    fahrer = (name, vorname)
    conn = DbContext.create_connection(database)
    (fid, message) = DbContext.select_fahrerId(conn, fahrer)
    if message == False:
        fid = DbContext.create_fahrer(conn, fahrer)
        return fid, "Fahrer created"
    else:
        return fid, "Fahrer allready exists"

def checkFahrzeug(polkz):
    conn = DbContext.create_connection(database)
    (fzid, message) = DbContext.select_fahrzeugId(conn, fahrzeug=polkz)
    if message == False:
        fzid = DbContext.create_fahrzeug(conn, fahrzeug=polkz)
        return fzid, "Fahrzeug created"
    else:
        return fzid, "Fahrzeug allready exists"

def parseFileName(filename):
    mylist = filename.split("_")
    fahrerName = mylist[0]
    name = fahrerName[0:1]
    vorname = fahrerName[1:2]
    polkz = mylist[1]
    return name, vorname, polkz

def overlayGPX(points, zoom,):
    # gpx_file = open(gpxData, 'r')
    # gpx = gpxpy.parse(gpx_file)
    # points = []
    # for track in gpx.tracks:
    #     for segment in track.segments:        
    #         for point in segment.points:
    #             points.append(tuple([point.latitude, point.longitude]))
    latitude = sum(p[0] for p in points)/len(points)
    longitude = sum(p[1] for p in points)/len(points)
    myMap = folium.Map(location=[latitude,longitude],zoom_start=zoom)
    folium.PolyLine(points, color="red", weight=2.5, opacity=3).add_to(myMap)
    return (myMap)


def main():
    
    gpxdir = r'C:\Users\Emre Kayabasi\Documents\gpxfiles\AA_WIT-AA000_001.gpx'
    overlayGPX(gpxdir, '14')

        

if __name__ == '__main__':
    main()