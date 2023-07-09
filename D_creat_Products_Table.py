import mysql.connector 
mydb =mysql.connector.connect(
    host="localhost",
    user ="root",
    password= 'Rakesh@1234',
    database ="rboutique"
)

mycursoe = mydb.cursor()

#Create Product tables 
try:
    mycursoe.execute("""CREATE TABLE products(
                  pro_num char(10),
                  pro_id char(10) PRIMARY KEY,
                  pro_price INT(6),
                  pro_stk INT(5)
                  )""")
except Exception:
    print("Table Exist!")


print("\n")

#Checking the table structure and data stored in the table

mycursoe.execute("DESC products")
myrs = mycursoe.fetchall()
for x in myrs:
    print(x)
    
    
print()

# Insert some products in products table 

try:
    sql = "INSERT INTO products (pro_num, pro_id, pro_price, pro_stk) VALUES(%s, %s, %s, %s)"
    val = [
        ('1','KWPTP25', 330, 18),
        ('2','KWPTP30', 450, 30),
        ('3','KWPTP45', 650, 20),
        ('4','SSST025', 850, 10),
        ('5','SSST030', 350, 12)
    ]

    mycursoe.executemany(sql,val)
    mydb.commit()
    print(mycursoe.rowcount, "record was inserted.")
except Exception:
    print("Simlear Data Can't store in Primary Key")
    
print("\n")



#Show data in Products Table

mycursoe.execute("SELECT * FROM products")
myrest = mycursoe.fetchall()
for y in myrest:
    print(y)