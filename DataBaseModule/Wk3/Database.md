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