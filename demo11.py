# demo11: Python MySQL Drop Database

# 1. importing MySQL Connector package:
import mysql.connector

# 2. Create Connection
mydb = mysql.connector.connect (
    host="localhost",
    user='root',
    passwd='root',
    # since we are going to use the same database in every py file for this project/folder
    # we can just add the following property:
    database ='mydatabase'
)

# 3. Creating an instance of a cursor
my_cursor = mydb.cursor()

query = "SHOW DATABASES"
my_cursor.execute(query)

# view the content of my_cursor object:
for db in my_cursor:
  print(db)

my_cursor.execute('DROP DATABASE mydatabase')

my_cursor.execute('SHOW DATABASES')
# view the content of my_cursor object:
for db in my_cursor:
  print(db)