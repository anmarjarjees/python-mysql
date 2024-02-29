# demo10: Python MySQL Drop Table

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

# Delete a Table
# You can delete an existing table by using the "DROP TABLE" statement:
query = "DROP TABLE clients"

# We will comment the execution line to avoid the deleting this table
# my_cursor.execute(query)

# remember that we used the same command DROP for deleting a full database:
# The syntax: DROP DATABASE database_name

# Drop Only if Exist
# If the the table you want to delete is already deleted, 
# or for any other reason does not exist, 
# you can use the "IF EXISTS" keyword to avoid getting an error
# if the table is not exists
query = "DROP TABLE IF EXISTS clients"

my_cursor.execute(query)