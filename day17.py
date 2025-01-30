# pip install mysql-connector-python
# import mysql.connector

# try:
#     db = mysql.connector.connect (
#         host = 'localhost',
#         username = 'root',
#         port = 3306, 
#     )

#     cursor = db.cursor()
#     cursor.execute("CREATE DATABASE student")
    
# except mysql.connector.errors.DatabaseError as e:
#     print(e)
    
# except mysql.connector.errors.IntegrityError as e:
#     print(e)

import mysql.connector

db = mysql.connector.connect (
    host = 'localhost',
    username = 'root',
    port = 3306, 
    database = 'student'
    )

cursor = db.cursor()
cursor.execute("CREATE TABLE student_details(name varchar(20), address varchar(20), phone int)")

