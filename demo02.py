# demo2: Python MySQL Create Table

# 1. importing MySQL Connector package:
import mysql.connector

# 2. Create Connection
mydb = mysql.connector.connect (
    host="localhost",
    user='root',
    passwd='root'
    # Besides specifying these three variables, we can also specify our database {Later...}
)

# 3. Creating an instance of a cursor
my_cursor = mydb.cursor()

# Before creating any table, we have to choose the wanted databases: "MyDatabase"
# Later we will learn how to add our database name to the connection string
# Using "MyDatabase" the one we created in demo01.py
my_cursor.execute('USE MyDatabase')

# Adding our first table in this database,
# Any table in a database SHOULD have a primary key (strongly recommended)
# Primary Key:
# When creating a table, you should also create a column with a unique key for each record.
# This can be done by defining a constraint "PRIMARY KEY".
# We use this statement in most of the time:
# "INT AUTO_INCREMENT NOT NULL PRIMARY KEY" 
# OR:
# "INT AUTO_INCREMENT PRIMARY KEY" 
# This "auto_increment" Primary Key: Which will insert a unique number for each record. 
# Starting at 1, and increased by one for each record.

# now we can create/add table(s) to the selected database:
# CREATE TABLE IF NOT EXISTS clients .....
my_cursor.execute("CREATE TABLE IF NOT EXISTS clients (first_name VARCHAR(50), last_name VARCHAR(50), email VARCHAR(50), address VARCHAR(100))")
# We Created our table without a primary key!

# Now we need to modify the table description by adding the PK
my_cursor.execute('DESC clients')
print(my_cursor) # MySQLCursor: DESC clients
print(type(my_cursor)) # <class 'mysql.connector.cursor.MySQLCursor'>
for item in my_cursor:
    print(item)

# The output:
# ('first_name', 'varchar(50)', 'YES', '', None, '')
# ('last_name', 'varchar(50)', 'YES', '', None, '')
# ('email', 'varchar(50)', 'YES', '', None, '')
# ('address', 'varchar(100)', 'YES', '', None, '')

# NOTE: If you run the statement "DESC clients" in MySQL, you will see these headings
# Field, Type, Null, Key, Default, Extra

# Adding a primary key:*************************************************************
# ALTER TABLE: For modifying the table structure and fields:
# If the table already exists, use the ALTER TABLE keyword to modify its properties:
# SQL: ALTER TABLE clients ADD COLUMN clientID INT AUTO_INCREMENT PRIMARY KEY
# NOTE: Dont forget to comment the code below the next time you run the code:
# my_cursor.execute('ALTER TABLE clients ADD COLUMN clientID INT AUTO_INCREMENT PRIMARY KEY')

# For checking how many tables we have in "mydatabase":
# my_cursor variable will be used to execute all SQL commands:
my_cursor.execute('SHOW TABLES')
print("Mydatabase Tables (Row Display):")
for table in my_cursor:
    # in every iteration we are going to print a table name
    print(table) # We only have one table so far => ('clients',)


# We need to rerun the same command again "my_cursor.execute()":
my_cursor.execute('SHOW TABLES') # we can use either ' or "
print("Mydatabase Tables (Nice Format):")
for table in my_cursor:
    # in every iteration we are going to print a table name
    print("Database Table: ",table[0]) # We only have one table so far => ('clients',)

# There is a better solution for this issue of keep repeating the SQL command {later...}