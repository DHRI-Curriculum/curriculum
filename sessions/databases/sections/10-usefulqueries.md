[<<< Back](9-importcsv.md) - [Next >>>](11-querieschallenge.md)  

# Querying to summarize your data  

Let's see what the nypl_items table looks like:  

1. How many records are in the table?  

	```sql
	SELECT COUNT(*) FROM nypl_items;  
	```  

2. What do the records look like?  

	```sql
	SELECT * FROM nypl_items LIMIT 3;
	```  

3. How many different languages do you have items in?  

	```sql
	SELECT DISTINCT language FROM nypl_items;
	```  

[<<< Back](9-importcsv.md) - [Next >>>](11-querieschallenge.md)