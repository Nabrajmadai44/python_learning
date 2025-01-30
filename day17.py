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
# cursor.execute("CREATE TABLE student_details(name varchar(20), address varchar(20), phone int)")

# cursor.execute("Insert into student_details (name, address, phone) values ('Nabraj', 'Dubaha', '9809438444')")
# db.commit()

# sql = "INSERT INTO student_details (name, address, phone) VALUES (%s, %s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4', 989),
#   ('Amy', 'Apple st 652', 23),
#   ('Hannah', 'Mountain 21', 23),
#   ('Michael', 'Valley 345', 23),
#   ('Sandy', 'Ocean blvd 2', 23),
#   ('Betty', 'Green Grass 1', 23),
#   ('Richard', 'Sky st 331', 23),
#   ('Susan', 'One way 98', 23),
#   ('Vicky', 'Yellow Garden 2', 23),
#   ('Ben', 'Park Lane 38', 23),
#   ('William', 'Central st 954', 23),
#   ('Chuck', 'Main Road 989', 23),
#   ('Viola', 'Sideway 1633', 23)
# ]
# cursor.executemany(sql, val)
# db.commit()

# n = int(input('Enter a limit: '))
n = 3
sql = f'select name , address from student_details limit {n}'

cursor.execute(sql)
data = cursor.fetchall()

for individual in data:
    print(individual[0], individual[1])



# db = mysql.connector.connect (
#     host = 'localhost',
#     username = 'root',
#     port = 3306, 
#     database = 'Nepse'
#     )

# cursor = db.cursor()
# cursor.execute("CREATE DATABASE Nepse")
# cursor.execute("CREATE TABLE Nepse_ShareMarket(name varchar(20), point int, percentage int, high int, low int)")
