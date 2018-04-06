[<<< Back](1-builddb.md) - [Next >>>](3-insertdata.md) 

# Building tables

The next step is to create tables to hold your data. From here onwards, we are going to execute database queries using the SQL editor to practice SQL syntax.
  
1. Open the SQL editor:

![To open SQL editor, click “Tools” and “Open SQL editor”](https://github.com/GCDigitalFellows/GCDRI_databases/blob/master/images/open_sql_ed.png)

Your SQLiteStudio interface should look like this:

 ![SQLiteStudio interface with SQL editor and databases window](https://github.com/GCDigitalFellows/GCDRI_databases/blob/master/images/sqlite_wkspace.png)

2. Create a table to store data about academic programs. Name the table "programs" and give it two fields (aka, columns): one for "id", the other for "program_name":

The syntax for creating a table in SQLite is:

```sql
CREATE TABLE table_name ( field_name data_type constraints )
```

- The [data type](https://www.sqlite.org/datatype3.html) will affect the behavior of the data in that field. For example, whether the data itself is treated as text or a number.  

- The [constraints](http://www.tutorialspoint.com/sqlite/sqlite_constraints.htm) will affect the behavior of that field. For example, a field with a `NOT NULL` constraint means that each record must have some data in this field.   
	
```sql
CREATE TABLE programs  (  
	id INTEGER PRIMARY KEY,  
	program_name VARCHAR  
);
```

Highlight the code you just entered in the SQL editor and click the blue triangle to execute it.
	
![Creating "programs" table](https://github.com/GCDigitalFellows/GCDRI_databases/blob/master/images/create_table.png)  
	
[<<< Back](1-builddb.md) - [Next >>>](3-insertdata.md) 
