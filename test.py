import mysql.connector

mydb = mysql.connector.connect(
    # since we are using our local machine (our computers), the host: "localhost"
    host="localhost",
    # remember by default, we left the user'name to be 'root'
    user='root',
    # Don't forget to use a very simple password, It has to be an exiting one!
    password='root', 
)

# for testing
print(mysql.connector)
# The result is below is just "an example":
# <module 'mysql' from:
# 'C:\\Users\\Alex Chow\\
# AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages\\
# mysql\\__init__.py'>

print (mydb)
