# demo6: Python MySQL WHERE clause with AND/OR operations

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

# Select With a Filter (conditional Statement)
# Task: Select all records that have:
# 1. the last names that start with "a" 
# 2. AND their ID's are greater than 10

# To recap
# my_cursor.execute('Putting here our SQL command as a string')
# Just another way to write the sql statement in a separate line
# Select With a Filter (conditional Statement):
query = "SELECT * FROM clients WHERE last_name LIKE 'a%' AND clientid>10"
my_cursor.execute(query)

# Note: We use the fetchall() method, which fetches all rows from the last executed statement.
result = my_cursor.fetchall()
print(result)

print("----------------------------------------------------")
# Or:
for record in result:
    print('Client ID:', record[4])
    print('Full name:', record[0], record[1])
    print('Email:', record[2])
    print('Address:', record[3])
    print('**********************************')

print('====================================================')


# Task: Select all the records where the first name OR last name starts with "a":
query = "SELECT * FROM clients WHERE first_name LIKE 'a%' OR last_name LIKE 'a%'"
my_cursor.execute(query)

# Quick review:
# remember that printing my_cursor will just return a the SQL statement
# print(my_cursor) # MySQLCursor: SELECT * FROM clients WHERE first_name L..
# Unless if you want to loop through my_cursor items/elements:
# for item in my_cursor: # this loop will display all the items we received from the query statement
#    print(item)


# Very Important Note:
# Please be advised if you use it without "fetchall()": 
# result2 = my_cursor.execute(query) 
# Then printing result2 ==> we will get None
# result2 = my_cursor.fetchall()
# Then printing result2 ==> will get the record if we have any match
result2 = my_cursor.fetchall()

print("First or Last names start with a:")
print(result2)