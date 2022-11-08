import DbContext


database = r"C:\Users\Emre Kayabasi\Neuer Ordner\gpx.db"
class Fahrer(object):

    def getFahrer():
        conn = DbContext.create_connection(database)
        (list, message) = DbContext.select_fahrer(conn)
        if message == False:
            return list, "False"
        else:
            return list, "true"

class Fahrzeug():

    def getFahrzeugIds(fid):
        conn = DbContext.create_connection(database)
        (list, message) = DbContext.select_fahrzeugIdFromFahrt(conn, fid)
        if message == False:
            return list, "False"
        else:
            return list, "true"

    def getFahrzeug(fzids):
        list = []
        conn = DbContext.create_connection(database)

        for fzid in fzids:
            (fahrzeug, message) = DbContext.select_fahrzeugById(conn, str(fzid))
            list.append(fahrzeug)

        return list

class Fahrt():
    def getFahrt(fid, fzid):
        conn = DbContext.create_connection(database)
        val = (fid , fzid)
        (list, message) = DbContext.select_fahrtByFidAndFzid(conn, val)
        if message == False:
            return list, "False"
        else:
            return list, "true"

    def getFahrtenBetweenDates(startDate, endDate):
        conn = DbContext.create_connection(database)
        val = (startDate , endDate)
        (list, message) = DbContext.select_fahrtByDate(conn, val)
        if message == False:
            return list, "False"
        else:
            return list, "true"


class Fahrtpunte():
    def getPoints(ftid):
        conn = DbContext.create_connection(database)
        val = ftid

        (points, message) = DbContext.select_PointsByFahrtId(conn, val)
        if message == False:
            return points, "False"
        else:
            return points, "true"

# def main():
#      Fahrtpunte.getPoints(2,'2019-01-02','2022-22-19')



# if __name__ == '__main__':
#     main()