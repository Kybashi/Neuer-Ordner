import DbContext

database = r"C:\DB\gpx\gpx.db"

class Fahrer(object):

    def getFahrer():
        conn = DbContext.create_connection(database)
        (list, message) = DbContext.select_fahrer(conn)
        if message == False:
            return list, "False"
        else:
            return list, "true"

class Fahrzeug():

    def getFahrzeug():
        conn = DbContext.create_connection(database)
        (list, message) = DbContext.select_fahrzeug(conn)
        if message == False:
            return list, "False"
        else:
            return list, "true"

def main():
     database = r"C:\DB\gpx\gpx.db"
     obj = Fahrer
     (list, status) = Fahrzeug.getFahrzeug()



if __name__ == '__main__':
    main()