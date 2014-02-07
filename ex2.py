#create sqllite database
#import sqlite3 
import sqlite3

#create database
conn=sqlite3.connect("new.db")
#get a cursor object
cursor=conn.cursor()
#execute sql query
cursor.execute("""CREATE TABLE population(city TEXT,state TEXT ,population INT)""")
#close connection
conn.close()
