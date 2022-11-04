import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_fahrer(conn):
    try:
        sql = ''' SELECT name, vorname FROM fahrer '''
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()

        if len(res) < 1:
            conn.row_factory = None
            return "", False
        else:
            conn.row_factory = None
            return res, True

    except sqlite3.Error as error:
        print("Failed to read data from fahrer table")
        return error

def select_fahrzeug(conn):
    try:
        sql = ''' SELECT polkz FROM fahrzeug '''
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()

        if len(res) < 1:
            conn.row_factory = None
            return "", False
        else:
            conn.row_factory = None
            return res, True

    except sqlite3.Error as error:
        print("Failed to read data from fahrzeug table")
        return error

def select_fahrtpunktId(conn, fahrer):
    try:
        conn.row_factory = lambda cursor, row:row[0]
        sql = ''' SELECT * FROM fahrtpunkt
              WHERE lat=? AND lon=? AND ele=? AND zeitstempel=? AND ftid=? '''
        cur = conn.cursor()
        cur.execute(sql, fahrer)
        res = cur.fetchall()
        if len(res) < 1:
            conn.row_factory = None
            return "", False
            
        else:
            conn.row_factory = None
            return res[0], True

    except sqlite3.Error as error:
        print("Failed to read data from farhtpunkt table")
        return error

def select_fahrerId(conn, fahrer):
    try:
        conn.row_factory = lambda cursor, row:row[0]
        sql = ''' SELECT * FROM fahrer
              WHERE name=? AND vorname=? '''
        cur = conn.cursor()
        cur.execute(sql, fahrer)
        res = cur.fetchall()
        if len(res) < 1:
            conn.row_factory = None
            return "", False
            
        else:
            conn.row_factory = None
            return res[0], True

    except sqlite3.Error as error:
        print("Failed to read data from fahrer table")
        return error

def select_fahrzeugId(conn, fahrzeug):
    try:
        conn.row_factory = lambda cursor, row:row[0]
        sql = ''' SELECT fzid FROM fahrzeug
              WHERE polkz=? '''
        cur = conn.cursor()
        cur.execute(sql, (fahrzeug,))
        res = cur.fetchall()

        if len(res) < 1:
            conn.row_factory = None
            return "", False
        else:
            conn.row_factory = None
            return res[0], True

    except sqlite3.Error as error:
        print("Failed to read data from fahrzeug table")
        return error

def select_fahrtId(conn, fahrt):
    try:
        conn.row_factory = lambda cursor, row:row[0]
        sql = ''' SELECT ftid FROM fahrt
              WHERE dateiname=? AND fid=? AND fzid=? '''
        cur = conn.cursor()
        cur.execute(sql, fahrt)
        res = cur.fetchall()

        if len(res) < 1:
            conn.row_factory = None
            return "", False
        else:
            conn.row_factory = None
            return res[0], True

    except sqlite3.Error as error:
        print("Failed to read data from fahrt table")
        return error

def create_fahrer(conn, fahrer):
    sql = ''' INSERT INTO fahrer(name,vorname)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, fahrer)
    conn.commit()
    return cur.lastrowid

def create_fahrzeug(conn, fahrzeug):
    sql = ''' INSERT INTO fahrzeug(polkz)
              VALUES(?) '''
    cur = conn.cursor()
    cur.execute(sql, (fahrzeug,))
    conn.commit()
    return cur.lastrowid

def create_fahrt(conn, fahrt):
    sql = ''' INSERT INTO fahrt(dateiname,fid,fzid)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, fahrt)
    conn.commit()
    return cur.lastrowid

def create_fahrtpunkt(conn, fahrt):
    sql = ''' INSERT INTO fahrtpunkt(lat,lon,ele,zeitstempel,ftid)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, fahrt)
    conn.commit()
    return cur.lastrowid

# def main():
#     database = r"C:\DB\gpx\gpx.db"


#     # create a database connection
#     conn = create_connection(database)
#     with conn:
#         fahrzeug = ('BOT-EK-1');
#         create_fahrzeug(conn, fahrzeug)


        

# if __name__ == '__main__':
#     main()