[<<< Back](3-insertdata.md) - [Next >>>](5-foreignkeys.md)

# Updating fields

You can alter tables after they've been created. The SQL syntax below adds another field to the existing table and then populates that field with data.

1. Add another field for "program_level" to the existing table:   

	```sql
	ALTER TABLE programs    --selects the "programs" table to update
	ADD program_level VARCHAR;    --adds a "program_level" column, which is a string
	```

	If the query was successful, your database should now look like this (you may need to hit the refresh button to see the changes):

	![Your database after adding the new "program_level" field](https://github.com/GCDigitalFellows/GCDRI_databases/blob/master/images/new_field.png)  



2. Now, let's populate the new empty "program_level" field with some data  

	```sql
	UPDATE programs		--select the table to update
	SET program_level = "Ph.D."		--select the field and value to update
	WHERE program_name = 'Linguistics';		--select the condition for updating
	```

### Challenge

Update the "program_level" field for "Biology" and "Anthropology" with "Master's".

Hint: You can do this with one statement using_ `IN`




#### Solution

```sql
UPDATE programs
SET program_level = "Master's"
WHERE program_name IN ("Anthropology", "Biology");
```
	
[<<< Back](3-insertdata.md) - [Next >>>](5-foreignkeys.md)
