# demo1: Python MySQL Connection, Test Connection, SQL SHOW DATABASES

# Test if the installation of MySQL was successful, 
# or if you already have "MySQL Connector" installed,
# create a Python page with the following content:

# NOTE: We HAVE to download mysql/connector tool
# Please refer to my lectures (The PDF files) for more details

# 1. importing MySQL Connector package:
# *************************************
# Import this module mysql.connector
# MySQL Connector/Python - MySQL driver written in Python
import mysql.connector

# 2. Create / Initialize a connection with MySQL:
# ***********************************************
# Start by creating a connection to the database.
# Creating an instance (object) of our database
# our instance/object name is "mydb" [You can pick any other name you prefer]
# Passing 3 variables to the connect() method:
# - host: the url for our database
# - user: the user's name
# - passwd: the same one you entered when you installed MySQL

mydb = mysql.connector.connect(
    # since we are using our local machine (our computers), the host: "localhost"
    host="localhost",
    # remember by default, we left the user'name to be 'root'
    user='root',
    # Don't forget to use a very simple password, It has to be an exiting one!
    passwd='root'  
    # PLEASE, PLEASE be advised that you have to change the password based on your settings
    # We have to user the same credential that we use with MySQL Shell/Workbench
)

# prove it or test the connection:
print(mydb)
# if the credentials are wrong: mysql.connector.errors.ProgrammingError
# mysql.connector.errors.ProgrammingError: Access denied for user 'root1'@'localhost'

# if the credentials are correct:
# <mysql.connector.connection.MySQLConnection object at 0x00BB8160>

# 3. Creating an instance of a cursor
# ***********************************
my_cursor = mydb.cursor()
# my_cursor variable will be used to execute all SQL commands:
# Think about "my_cursor" as a pointer to point to our database and run/execute SQL statement
# for testing:
print (my_cursor) # output: MySQLCursor: (Nothing executed yet)

# Task: Show databases:
# SQL Commands: SHOW DATABASES
# The syntax: my_cursor.execute(' Write your SQL Statement ')
# NOTE: Dont forget to comment the code below the next time you run the code:
my_cursor.execute('SHOW DATABASES') # we can use either ' or "
print (my_cursor) # MySQLCursor: SHOW DATABASES

# my_cursor might have one or more databases
# execute() Python method will return a list
# we need to loop through my_cursor databases
for db in my_cursor:
    # in every iteration we are going to print a database name
    print(db)

# ('abc_school',)
# ('cbc_college',)
# ('challengedb',)
# ('chinook',)
# ('highend_college',)
# ('information_schema',)
# ('mysql',)
# ('nice_melodies',)
# ('performance_schema',)
# ('sys',)

# We need to rerun the same command again:
# We don't like this format:
# ('abc_school',) <== it's a list (array) and the db name 'abc_school' has index 0
# ('challengedb',) <== it's a list (array) and the db name challengedb' has index 0

# We like this format:
# Database Name: abc_school
# Database Name: challengedb
# Just for checking again:
print (my_cursor) # MySQLCursor

print ('Another nice output format:')
# We still need to run this command again
my_cursor.execute('SHOW DATABASES')
for db in my_cursor:
    # we can use the list syntax 
    # all the databases are saved in index 0
    print ("Database Name: ",db[0])


# Before closing this demo01, 
# let's create a new database for learning Py and MySQL
# our database name is "mydatabase"
# SQL Command: "CREATE DATABASE mydatabase"

# Delete it if it's exist:
my_cursor.execute('DROP DATABASE mydatabase')

# Create a new one:
my_cursor.execute('CREATE DATABASE MyDatabase')









