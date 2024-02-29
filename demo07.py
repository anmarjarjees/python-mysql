# demo7: Python MySQL Where with ORDER BY

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

# Sort the Result:
# Use the ORDER BY statement to sort the result in ascending (default) or descending order.
# The ORDER BY keyword sorts the result in ascending order by default. 
# To sort the result in descending order, use the DESC keyword at the end

# Task: Select all the records for any client id greater than 5
# And display the result in alphabetical order [A-Z] based on the first_name field
my_cursor.execute("SELECT * FROM clients WHERE clientID>5 ORDER BY first_name")

# Note: We use the fetchall() method, which fetches all rows from the last executed statement.
result =my_cursor.fetchall()

print (result)

print("----------------------------------------------------")
# Or:
for record in result:
    print('Client ID:', record[4])
    print('Full name:', record[0], record[1])
    print('Email:', record[2])
    print('Address:', record[3])
    print('**********************************')

print('=====================================================')


# Task: 
# Select records where the first name OR last name starts with "a":
# Sort the result "desc" => [Z-A] by the first_name column:
query="SELECT * FROM clients WHERE first_name LIKE 'a%' OR last_name LIKE 'a%' ORDER BY first_name DESC"
my_cursor.execute(query)

result2 = my_cursor.fetchall()
print("First or Last names starts with a in descending order:")
print(result2)

# using LIMIT keyword
# Task: We want to return/select the top five records
my_cursor.execute("SELECT * FROM clients LIMIT 5") # LIMIT 5 => will return the top five records
result3=my_cursor.fetchall()
print("_________________________________________________________")
print("TOP 5 Records in the table (No order)")
print("-------------------------------------")
for record in result3:
    print('Client ID:', record[4])
    print('Full name:', record[0], record[1])
    print('Email:', record[2])
    print('Address:', record[3])
    print('**********************************')

# Using LIMIT x, we give us only the top x records (x=2,x=5, or any value)
# What if we want to select the top 3 records 
# starting for the second one (skipping the first record) !?!?

# Starting From Another Position
# you can use the "OFFSET" keyword:

# using LIMIT keyword with OFFSET
# SELECT the first 3 records but not the first one
my_cursor.execute("SELECT * FROM clients LIMIT 3 OFFSET 1")
result4=my_cursor.fetchall()
print("_________________________________________________________")
print("TOP 3 Records in the table Except the first one (No order)")
print("-------------------------------------")
for record in result4:
    print('Full name:', record[0], record[1])
    print('Email:', record[2])
    print('Address:', record[3])
    print('**********************************')