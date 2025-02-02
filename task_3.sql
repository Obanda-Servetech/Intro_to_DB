-- Use the INFORMATION_SCHEMA database
USE INFORMATION_SCHEMA;

-- Select table names from the 'tables' table where the table schema matches 'alx_book_store'
SELECT table_name
FROM tables
WHERE table_schema = 'alx_book_store';

