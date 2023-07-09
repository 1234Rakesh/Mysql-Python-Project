import mysql.connector 

mydb = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password ="Rakesh@1234",
    database ="rboutique"
)

mycursoe = mydb.cursor()

#Creating a Employee table
try:
  mycursoe.execute("""CREATE TABLE employee(
                  emp_id char(3) PRIMARY KEY,
                  e_nam VARCHAR(30),
                  e_lnam VARCHAR(30),
                  e_phno VARCHAR(10),
                  e_adrs VARCHAR(30)
                )""")
except Exception:
  print("Table Existed!")


#Checking the table structure and data stored in the table

mycursoe.execute("DESC employee")
myres = mycursoe.fetchall()
for x in myres:
  print(x)