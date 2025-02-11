import mysql.connector
from mysql.connector import Error

myconn=mysql.connector.connect(host="localhost", user="root", password="1234", database="PYTHON_DB")
cur=myconn.cursor()
cur.execute("SELECT * from python_db")
all=cur.fetchall()
print(len(all))
print(all)
for row in all:
    print(row)
    print(x)
    print(all[0])
    print(all[1])
    print(all[2])
    print(all[3])
    print(all[4])
