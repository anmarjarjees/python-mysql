# demo3: Python MySQL Insert Into Table

# 1. importing MySQL Connector package:
import mysql.connector

# 2. Create Connection
mydb = mysql.connector.connect (
    host="localhost",
    user='root',
    passwd='root'
)

# 3. Creating an instance of a cursor
my_cursor = mydb.cursor()

# Before doing anything, we have to choose the wanted databases: "MyDatabase"
my_cursor.execute('USE MyDatabase')

# Adding one record
# Insert one single row
# my_cursor.execute('Put my SQL Command')
# or we can create a new variable for SQL Commands and pass these variable(s) to execute() function
# In the code below, we skipped the clientID because it's "AUTO_INCREMENT"
# my_cursor.execute("INSERT INTO clients (first_name,last_name,email,address) VALUES ('Martina','Smith','masmith@yahoo.ca','123 Yonge St.')")

# Very Important NOTE: Notice the statement: mydb.commit() is required to make/apply the changes, 
# Otherwise no changes are made to the table! Yes, it's the fact
# committing our code is required for any record modifications: Adding/Updating/Deleting record
mydb.commit()

# We can use this structure:
# sql_query=' Any SQL Statement '
# my_cursor.execute(sql_query)
sql_query="INSERT INTO clients (first_name,last_name,email,address) VALUES ('Martinos','Smith','mosmith@yahoo.ca','123 Yonge St.')"
# my_cursor.execute(sql_query)

# Don't forget to commit your code please:
mydb.commit()


# Adding another record (we will learn another way to add a record using python templates)
# we are adding a placeholder %s ==> for adding a string
# NOTE: please be advised if we have numeric values like age, average, salary
# => We DONT't put them in quotation marks
sql_query='INSERT INTO clients (first_name,last_name,email,address) VALUES (%s,%s,%s,%s)'
# Now we can create another Python variable for these values
record_values = ('Jessica','Simpson','jsimpson@yahoo.ca','654 Yonge St.')
# Now we can merge the sql_query and record_values variables together with execute() method
# Don't forget that I had to comment the following
# my_cursor.execute(sql_query,record_values)

# Don't forget to commit your code please:
mydb.commit()

# Let's try to run the SELECT command to view all the records:
my_cursor.execute('SELECT * FROM clients')
print(my_cursor) # MySQLCursor: SELECT * FROM clients !!!!!! We need to use for loop again:

# RAW Display! Boring or not clear:
for record in my_cursor:
    print(record)

# NOTE: Don't forget that:
# We already used the object my_cursor before
# We need to repeat the same SQL command again:
my_cursor.execute('SELECT * FROM clients')

# Or better one:
# we can use the index values to retrieve the info
print("The same result with labels (nice format):")
for record in my_cursor:
    # using the index => record[ index_value ]
    # record[0] => will return the value of the first_name field(column)
    # record[1] => will return the value of the last_name field(column)
    # and so on for the rest
    print('Client ID: ', record[4])
    print('Full Name: ', record[0],record[1]) # Full Name: Martina Smith
    print('Email:', record[2])
    print('Address:', record[3])
    print('**********************************')


# Adding more than one record at time:
# Insert Multiple Records (Rows)
# The pure SQL statement:
"""
INSERT INTO clients (first_name,last_name,email,address) 
VALUES 
('Peter', 'Smith', 'msmith@email.ca', '123 Yonge St.'),
('Amy', 'Clarck', 'amy@email.ca', '123 Yonge St.'),
('Viola', 'Alton', 'voila@email.ca', '123 Yonge St.'),
('Vicky', 'Williams', 'vicky@email.ca', '123 Yonge St.'),
('Sandy', 'Simpsons', 'sandy@email.ca', '123 Yonge St.')
"""

# We can use the more organized way:
# the placeholders %s
# one python variable for the SQL
# another python variable for the values
sql_query='INSERT INTO clients (first_name,last_name,email,address) VALUES (%s,%s,%s,%s)'
# We need to insert multiple record NOT just only one!
# To save multiple values into a single variable, this variable has to be a list (array)
many_record_values = [ 
    ('Peter', 'Smith', 'msmith@email.ca', '123 Yonge St.'),
    ('Amy', 'Clarck', 'amy@email.ca', '123 Yonge St.'), 
    ('Viola', 'Alton', 'voila@email.ca', '123 Yonge St.'),
    ('Vicky', 'Williams', 'vicky@email.ca', '123 Yonge St.'),
    ('Sandy', 'Simpsons', 'sandy@email.ca', '123 Yonge St.')
]

# Now we can merge these two variables:
# - sql_query 
# - many_record_values 
# with executemany() method

# To insert multiple rows into a table, we use the executemany() method.
# The second parameter of the executemany() method is a list of tuples, 
# containing the data you want to insert:
my_cursor.executemany(sql_query,many_record_values)

# Don't forget to commit your code please:
mydb.commit()

# A very good/friendly message to print ==> using the property "rowcount"
# using property called "rowcount" return a number of how many rows have been affected
# since we want to insert rows, we can write "row(s) inserted"
print(my_cursor.rowcount,"row(s) inserted")