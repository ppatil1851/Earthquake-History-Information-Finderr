import sqlite3 as sql
import csv
con= sql.connect("earth.db")
cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS dbo.earthquake")
    #Create SQL Table
sql ='''CREATE TABLE earthquake (
        "time"	TEXT,
        "latitude"	REAL,
        "longitude" REAL,
        "depth" REAL,
        "mag" REAL,
        "magType" TEXT,
        "nst" INTEGER,
        "gap" REAL,
        "dmin" REAL,
        "rms" REAL,
        "net" TEXT,
        "id" TEXT,
        "updated" TEXT,
        "place" TEXT,
        "type" TEXT,
        "horizontalError" REAL,
        "depthError" REAL,
        "magError" REAL,
        "magNst" INTEGER,
        "status" TEXT,
        "locationSource" TEXT,
        "magSource" TEXT)'''
cur.execute(sql)
a_file = open("static/allmonth.csv",  encoding='utf-8')
rows = csv.reader(a_file)
print(rows)
cur.executemany("INSERT INTO earthquake VALUES (?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", rows)

con.commit()
con.close()