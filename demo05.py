# demo5: Python MySQL WHERE clause
# adding some conditions/filters 

 # 1. importing MySQL Connector package:
import mysql.connector

# 2. Create Connection
mydb = mysql.connector.connect (
    host="localhost",
    user='root',
    passwd='root',
    # since we are going to use the same database 
    # in every py file for this project/folder
    # we can just add the following property:
	# to connect our files to the same database "mydatabase"
    database ='mydatabase'
)

# 3. Creating an instance of a cursor
my_cursor = mydb.cursor()

# **************************************************************************************
# NOTE: We DON't need to use the code below:
# We already specified the database name that we want to use inside mysql.connector.connect
# my_cursor.execute('USE mydatabase') # This line is optional (we can omit it)
# **************************************************************************************

# Select With a Filter (conditional Statement)
# Task: all clients with id value greater than 10
my_cursor.execute('SELECT * FROM clients WHERE clientID>10')

# Note: We use the fetchall() method, 
# which fetches all rows from the last executed statement.
result =my_cursor.fetchall()

# for test
# print (result)

print("----------------------------------------------------")
# Or: display them with a nice format and labels:
for record in result:
    print('Client ID:', record[4]) # Our id field is the last :-(, but we place it first :-)
    print('Full name:', record[0], record[1])
    print('Email:', record[2])
    print('Address:', record[3])
    print('**********************************')

# Task: Select all records with last name value of "alton"
my_cursor.execute("SELECT * FROM clients WHERE last_name='alton'")
last_name_result = my_cursor.fetchall()
print("Result Based On Last Name:")
print(last_name_result) # print all that have last name "Alton"

# and so on, you can practice any WHERE Clause syntax as we did with MySQL
# ********************
# Wildcard Characters:
# ********************
# ********************
# You can also select the records that starts, includes, or ends with a given letter or phrase.
# Use the %  to represent wildcard character(s):
# Notice that Wild Cards work with "LIKE" SQL keyword (NOT the = sign)
# We can just change the "=" with "LIKE"

# Examples:
# Searching for all the records that have the first name starts with "A" or "a"
# this symbol % means any character and any number of characters and it could be NULL also
# example of this: a%
# Allen, Alex, Alena, Ali, and so on.... a%

# Task: Select all the records that have the first name starts with "A" or "a"
my_cursor.execute("SELECT * FROM clients WHERE first_name LIKE 'a%' ")
fnames_start_with_a =my_cursor.fetchall()

print("First names start with a:")
print(fnames_start_with_a)
print('==========================================================')

# Task: Select all the records that have the first name field value ending with "a"
my_cursor.execute("SELECT * FROM clients WHERE first_name LIKE '%a'")
fnames_end_with_a =my_cursor.fetchall()

# Task: Select all the records where the last name contains the word/text/letters "mi":
# examples: Smith, Mimos, Mayami, Kamil
my_cursor.execute("SELECT * FROM clients WHERE last_name LIKE '%mi%'")
lnames_contain_mi =my_cursor.fetchall()

print("Last names that contains 'mi':")
print(lnames_contain_mi)
print('==========================================================')