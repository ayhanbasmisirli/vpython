#Insert command
#import the sqllite3 library
import sqlite3

#create the connection object
conn =sqlite3.connect('new.db')

#get the cursor object used to execute SQL commands
cursor= conn.cursor()


#insert data

cursor.execute("INSERT INTO population VALUES('New York City','NY',8000000)")
cursor.execute("INSERT INTO population VALUES('San Francisco','CA',6000000)")

#commit changes

conn.commit()

conn.close()