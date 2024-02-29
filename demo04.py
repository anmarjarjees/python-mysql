 # demo4: Python MySQL Select From Table

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

# Before doing any thing, we have to choose the wanted databases: "MyDatabase"
my_cursor.execute('USE MyDatabase')

my_cursor.execute("SELECT * FROM clients")

# fetchall() Method:
# Note: If you want to save the result in the execute statement into a variable 
# to be used over and over as many times as we need in our code
# We can use the fetchall() method, 
# which fetches all rows from the last executed statement
# Just create another python variable:
result = my_cursor.fetchall()

print("----------------------------------------------------")
# for test:
print ("The result: ",result)
# Example of the result:
# [
# ('Martina', 'Smith', 'masmith@yahoo.ca', '123 Yonge St.', 13),
# ('Martinos', 'Smith', 'mosmith@yahoo.ca', '123 Yonge St.', 14), 
# ('Martina', 'Smith', 'masmith@yahoo.ca', '123 Yonge St.', 15),
# ('Jessica', 'Simpson', 'jsimpson@yahoo.ca', '654 Yonge St.', 17)
# ]

print("Print Each Record:")
for record in result:
    print(record)

print("**********************")
print("Print Each Record with its label:")
for record in result:
   print('Client ID:', record[4])
   print('Full name:', record[0], record[1])
   print('Email:', record[2])
   print('Adress:', record[3])
   print('**********************************')

# fetchone() Method:
# If you are only interested in one row, you can use the fetchone() method.
# The fetchone() method will return the FIRST RECORD (ROW) of the result:
my_cursor.execute("SELECT * FROM clients")
# fetchone: will return the fields (columns) of the first record only
first_record=my_cursor.fetchone()

# for test:
print ("The only one result: ",first_record) 
# The only one result:  ('Martina', 'Smith', 'masmith@yahoo.ca', '123 Yonge St.', 13)

# for test:
print("type: ",type(first_record)) ## type:  <class 'tuple'>

# We can see that one record is a list of fields (columns)
for field in first_record:
  print(field)

# Output Example:
# Martina
# Smith
# masmith@yahoo.ca
# 123 Yonge St.
# 13

# print all the fields of each record in one line:
# 3 Martin Smith msmith@yahoo.ca 123 Yonge St.
# 12 Martina Smith masmith@yahoo.ca 123 Yonge St.12

# please remember that the variable "result" 
# contains all the record from fetchall() function above
print('=====================================================')
print ('All records in one line:')
for record in result:
  # the id field, first name, last name, email, address
  print(record[4], record[0],record[1],record[2],record[3])


# Below we are using %s and tabs:
print('=====================================================')
print ('All fields of each record in one line using % s and tab:')
for record in result:
  print("Client ID: %s" %record[4]+ "\tFirst Name: %s" %record[0] +"\tLast Name: %s" %record[1]+"\tEmail: %s" %record[2]+"\t\tAddress: %s" %record[3])

print('=====================================================')
print ('All fields of each record in one line using % s and % but with Top Headings:')
# adding headers:
print ("Client ID\tFirst Name\tLast Name\tEmail\taddress")
for record in result:
  print("%s" %record[4]+ "\t\t%s" %record[0] +"\t\t%s" %record[1]+"\t\t%s" %record[2]+"\t\t%s" %record[3])

# Below we just tried to imagine displaying the result in an html page using Flask and Jinja:
# <table>
    # <tr>
        # <th>Client ID</th>
        # <th>First Name</th>
        # <th>Last Name</th>
        # <th>Email</th>
        # <th>Address</th>
    # </tr>
# {% for record in result: %}
    # <tr>
        # <td>{{ record[4] }}</td>
        # <td>{{ record[0] }}</td>
        # <td>{{ record[1] }}</td>
        # <td>{{ record[3] }}</td>
    # </tr>
# {% endfor %}
# </table>
