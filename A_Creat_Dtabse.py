import mysql.connector 

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Rakesh@1234"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE rboutique")