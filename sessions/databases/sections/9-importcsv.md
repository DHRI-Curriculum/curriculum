[<<< Back](8-innerjoin.md) - [Next >>>](10-usefulqueries.md)

# Import data into table  

Let's create a database table from an [existing csv file](https://github.com/GCDigitalFellows/nypl_data/blob/master/nypl_items.csv).

1. Create a table with a field for each column in the csv file that we want to import

	```sql
	CREATE TABLE nypl_items (
		id INTEGER PRIMARY KEY,
		title VARCHAR,
		contributor VARCHAR,
		year VARCHAR,
		language VARCHAR,
		description VARCHAR,
		note VARCHAR,
		subject VARCHAR,
		resource VARCHAR,
		genre VARCHAR,
		publisher VARCHAR,
		place VARCHAR,
		url VARCHAR
	);
	```


2. Double click on the table "nypl_items" in the databases window and click on the import icon  

![Importing a csv file to a new table](https://github.com/GCDigitalFellows/GCDRI_databases/blob/master/images/csv_import.png)

3. Follow import instructions

[<<< Back](8-innerjoin.md) - [Next >>>](10-usefulqueries.md)
