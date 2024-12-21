import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Samarth2002#",
)

cursor = dataBase.cursor()

cursor.execute("CREATE DATABASE dcrm")

cursor.execute("SHOW DATABASES")
