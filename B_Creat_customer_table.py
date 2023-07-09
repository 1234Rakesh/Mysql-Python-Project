import mysql.connector 

mydb = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password ="Rakesh@1234",
    database = "rboutique"
)

mycursoer = mydb.cursor()

try:
  mycursoer.execute("""CREATE TABLE customer (
                    cust_id INT(10) PRIMARY KEY,
                    c_nam VARCHAR(30),
                    c_lnam VARCHAR(30),
                    C_phon VARCHAR(10),
                    C_adrs VARCHAR(255),
                    bkd_pro VARCHAR(40)  
                      )""")
except Exception:
  print("Table Exists!")
  
mycursoer.execute("DESC customer")  
myrs = mycursoer.fetchall()
for x in myrs:
  print(x)
