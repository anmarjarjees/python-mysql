# demo9: Python MySQL Delete Record(s) From a table

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

# Delete Record
# You can delete record(s) from an existing table by using the "DELETE FROM" statement:
# Please DON'T forget WHERE clause

# Task: Delete the records the has id value of "22" <= int value
query = 'DELETE FROM clients WHERE clientid = 22'
my_cursor.execute(query)

# Important!: Notice the statement: mydb.commit().
# It is required to make the changes, otherwise no changes are made to the table.

# Notice the WHERE clause in the DELETE syntax: 
# The WHERE clause specifies which record(s) that should be deleted. 
# If you omit the WHERE clause, all records will be deleted!
mydb.commit()

print(my_cursor.rowcount, "record(s) deleted")

# Noticed here below, we used our original basic way to get the record (no fetchall)
print("The same result with labels:")
my_cursor.execute('SELECT * FROM clients')
for record in my_cursor:
    print('Client ID:', record[4])
    print('Full name:', record[0], record[1])
    print('Email:', record[2])
    print('Address:', record[3])
    print('**********************************')
