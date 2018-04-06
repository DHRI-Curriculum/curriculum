# SQLite “cheat sheet”

## Tips!
1. SQL is not case sensitive
2. End each SQL statement with a semicolon “;”
3. Use “*” to select an entire record
4. White space doesn’t matter
5. `SELECT` statement is like creating a new table
6. Field value needs to be in quotes
7. Use parentheses to force order of operations
8. Use two hyphens “--” to comment 

## C.R.U.D.

### Create
1. `CREATE DATABASE db_name` - creates a database

2. `CREATE TABLE table_name (field_name DATA_TYPE CONSTRAINTS)` - creates a table in the database
  1. Data types
    1. `DATE`
    2. `TIME`
    3. `TIMESTAMP`
    4. `VARCHAR/CHARACTER`
    5. `BOOLEAN`
    6. `INTEGER`
    7. `DOUBLE PRECISION (FLOAT)`
    8. `XML`

  2. Constraints
    1. `PRIMARY KEY`
    2. `FOREIGN KEY`
    3. `UNIQUE`
    4. `DEFAULT`
    5. `AUTOINCREMENT`
    6. `NOT NULL`

3. `INSERT INTO table_name(field1, field2) VALUES ('value1', 'value2')` - insert data into a table for one record

4. `INSERT INTO table_name(field1) VALUES (record1), (record2), (record3)` - insert data into a table for multiple records


### Read
#### This is the basic format for querying a database

1. `SELECT field1, field2` - select fields to return (or `*` to return entire record)

2. `FROM table_name` - select the table

3. `INNER JOIN table1, table2` - specify which tables to pull data from

4. `ON table1.field_a = table2.field_b` - specify which records to return from the join operation (`JOIN` + `ON` creates a temporary table that includes data from *table1* and *table2* for only those records where the value in *table1.field_a* is equal to the value in *table2.field_b*)

5. `WHERE table.field_a = "value_x"` - only returns records whose value for *field_a* is equal to *value_x* (`WHERE` acts like filter)

    1. `WHERE table.field_a IN ("value_x", "value_y", "value_z")` - only return records whose value for *field_a* is one of values in the parentheses (`NOT IN` - does the opposite)

    2. `WHERE table.field_a = value_x AND table.field_b = value_y` - only returns records where both conditions are met

    3. `... field_a = value_x OR field_b = value_y`

    4. `... field_a BETWEEN value_x AND value_y`

    5. `... field_a LIKE "spa%"` - return only records whose value in field_a starts with "spa"

    6. `<`, `<=`, `>`, `>=`, `!=`  

    7. `BETWEEN`  

    8. `IS` - equal to a value (or empty for `IS NULL`)

    9. `IS NOT` - is not equal to a value (or is not empty for `IS NOT NULL`)

6. `ORDER BY field_a ASC/DESC` - format how results are displayed - arrange records returned by values in *field_a* according to ascending order (`DESC` for descending order)


#### Misc.
1. `SELECT DISTINCT field_a FROM table` - return only distinct values for *field_a*

2. `SELECT COUNT(*) FROM table` - return the number of records in the table

3. `SELECT * FROM table LIMIT 5` - return only the first 5 records from the table


### Update
1. `ALTER TABLE table_name RENAME TO new_table_name` - rename a table

2. `ALTER TABLE table_name ADD COLUMN new_field_name DATA_TYPE CONSTRAINTS` - add a new field to a table (include data type and field constraints)

3. `UPDATE table SET field_a = value_x WHERE field_b = value_y` - add new data to one or more fields in a table


### Delete
1. `DELETE FROM table WHERE field = value` - delete data from a table

2. `DROP TABLE table_name` - delete a whole table


