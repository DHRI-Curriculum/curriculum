# import sqlite3 library
import sqlite3

# connect to the database (include path if db is in different directory)
conn = sqlite3.connect('nypldb.db')

# create a cursor object  
cur = conn.cursor()

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