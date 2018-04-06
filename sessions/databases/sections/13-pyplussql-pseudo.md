[<<< Back](12-excel_v_db.md) - [Back to top >>>](../README.md)

# SQL + Python = Awesome!

You can create a program to interact with a database by embedding SQL syntax in a Python script (using the sqlite3 library, which comes standard with every Python install)

Let's write a short program that asks a user for a place name and returns all records from the database that contain the value in the "place" field.  

0\. Using a text editor, create a file called "nypl_search.py" in the directory where the database containing the "nypl_items" table is located.

1\. Write some pseudocode in "nypl_search.py" that describes what our code will do once it's finished:

```Python
# import sqlite3 library

# connect to the database

# say hello to the user

# ask the user for a place

# search the place field in the "nypl_items" table for the place name

# return a list of records from the database that are from the place name
```

2\. Import the sqlite3 library, connect to the database, and create a cursor object. (Don't worry about this last part!)

```Python
# import sqlite3 library
import sqlite3

# connect to the database
conn = sqlite3.connect('nypldb.db')

# create a cursor object  
cur = conn.cursor()
```  

3\. Replace pseudocode with working Python and SQL

```Python
# say hello to the user
print("Hello! I will search your database for items from any place you tell me! ")

# ask the user for a place name
place_name = input("Please give me a place name: ")

# search the place field for the place name
cur.execute("SELECT * FROM nypl_items WHERE place = ?", (place_name,))

# return a list of records from the database that contain the keyword
record_list = cur.fetchall()

for i in record_list:
	print("\n\n", i)
``` 

4\. Run the program. First, open the command line, `cd` to the directory containing your "nypl_search.py" file and "nypldb.db" database. Then type 

    python nypl_search.py
	
and hit Enter. You'll be prompted to enter a place name, which is case-sensitive. Try "Paris" or some other location, and you should see output from the database returned to you.

Congratulations! You've successfully accessed your database using a Python script. This is an excellent first step in performing data analysis on large data sets or creating your own applications!

[<<< Back](12-excel_v_db.md) - [Back to top >>>](../README.md)
