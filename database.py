import mysql.connector
from mysql.connector import Error

connection = None

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="PYTHON_DB"
    )
    
    if connection.is_connected():
        print("Connected to MySQL server")
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")
        record = cursor.fetchone()
        print("Connected to database:", record)
        
except Error as e:
    print("Error while connecting to MySQL:", e)
    
finally:
    if connection and connection.is_connected():
        cursor.close()
        connection.close()