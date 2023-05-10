import sqlite3

connection = sqlite3.connect("testDatabase.db")
query = "INSERT into Table1(name,age,dept) values('Usman', 20 , 'CS');"
try:
    cursor = connection.cursor()
    #here CREATE TABLE is the command to create table in db, then type table name i.e Table1, then in bracket you type table attribute,
    #then you type data type i.e INTEGER, then type it's type i.e PRIMARY KEY, then type AUTOINCREMENT which'll increment it's values
    # connection.execute('''CREATE TABLE Table1(table1id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT(20) NOT NULL, age INTEGER, Dept TEXT(20));''')
    cursor.execute(query)
    connection.commit()
    print("Connection Successful and Table Created")


except:
    print("Connection failed")

connection.close()


# -------------------------
#how to fetch all data from sql table
connection = sqlite3.connect("testDatabase.db")
cursor=connection.cursor()
cursor.execute("SELECT * FROM Table1")

while True:
    record = cursor.fetchone()
    if record == None:
        break
    print(record)


# -------------------------
#how to update in sql 

try:
    cursor.execute("UPDATE Table1 SET age=25 WHERE name ='Usman';")
    connection.commit()
    print("successfully updated")
except:
    print("Failed updating sql")

# -------------------------
#how to delete in sql

try:
    cursor.execute("DELETE FROM Table1 WHERE Table1id = 3 ; ")
    connection.commit()
    print("successfully deleted")
except:
    print("Failed deleting entry")
