# demo8: Python MySQL Update Table Record

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

# Note: Please remember that we can modify/edit/change the table by:
# Modifying the table structure like adding/removing/updating fields (columns) => ALTER TABLE
# Modifying the record(s)/the data inside our table => UPDATE and SET keywords

# Update the Table record(s)
# You can update existing records in a table by using the "UPDATE" statement:
# Notice the WHERE clause in the UPDATE syntax: 
# The WHERE clause specifies which record or records that should be updated. 
# If you omit the WHERE clause, all records will be updated!
# So please DO NOT forget to add the "WHERE" clause with update statement
# The keywords for any update statement: UPDATE, SET, and WHERE Clause 

# Task: update clients table:
# change first name to be "Alexa" and last name to be "Chowing"
# change the email to be "alexachow@yahoo.ca"
# ONLY for the record with id=15
query="UPDATE clients SET first_name='Alexa', last_name='Chowing',email='alexachowing@yahoo.ca' WHERE clientid=15"

# Syntax: my_cursor.execute('SQL Command')
my_cursor.execute(query)

# Important!: Notice the statement: mydb.commit().
# It is required to apply the changes, otherwise no changes are made to the table.
mydb.commit()

# Using again the property .rowcount
print(my_cursor.rowcount, "record(s) updated") # 1 record(s) updated

# Noticed here below, we used our original basic way to get the record (no fetchall)
print("The same result with labels:")
my_cursor.execute('SELECT * FROM clients')
for record in my_cursor:
    print('Client ID:', record[4])
    print('Full name:', record[0], record[1])
    print('Email:', record[2])
    print('Address:', record[3])
    print('**********************************')

# Note: The update/delete statements will affect only the record(s) that match the WHERE condition