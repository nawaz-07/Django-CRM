import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd= 'root'
)

#preparing a cursor object
cursorobj=dataBase.cursor()

#create a database
cursorobj.execute("CREATE DATABASE oryxdb")
print("all done!")