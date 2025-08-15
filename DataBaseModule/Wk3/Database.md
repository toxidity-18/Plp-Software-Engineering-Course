#  Data manipulation and transaction .

## Data manipulation language .
- We use 2 major clauses i.e :

  - ```sql
      INSERT INTO . . . (NB: This is where you select specific columns you want to insert data into )
    VALUE (Insert data/ row as per the columns available) 
    -- NB Data inside () are usually sep by commas .
    -- NB Column === data .
    -- DESCRIBE . .  . Inspect columns for the selected table .
    -- SHOW COLUMNS FROM . . . ' for the selected tables .'
    -- CREATE DATABASE . . . This create the database .
    -- USE 'DATABASE' . . .
    -- CREATE TABLES  table_name( column associated with that table) 
    /*  UPDATE table_name
              SET 
                column_name = new_value 
              WHERE 
                 primary_key = num_of_primary_key
    */
     -- DELETE FROM   table_name   WHERE primary_key = num_of_primary_key

### More Resource :
* [INSERT](https://www.w3schools.com/SQl/sql_insert.asp)


# ACID Properties for transaction .
- Atomicity : all or nothing i.e when sending money transfer through mobile-payment options .
- Consistency : they follow certain rule when making transaction , i.e when send more money than one is your balances .Thus stop invalid data from messing up the database .
- Isolation : When transaction are taking place from 2 different people it makes sure that this transaction do not affect one another .
- Durability : make sure that changes made are permanent thus they are not affected when certain failures or outages occurs .

### More Resources :
[ACID](https://www.geeksforgeeks.org/acid-properties-in-dbms/)