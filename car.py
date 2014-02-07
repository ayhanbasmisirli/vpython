import sqlite3

conn =sqlite3.connect("car.db")
cursor =conn.cursor()
cursor.execute("""CREATE TABLE car (make TEXT ,model TEXT,quantity INT)""")
conn.close()
