-- This script removes all records from the table second_table with a
-- score of 5 or lower in the specified database.
DELETE FROM second_table
WHERE score <= 5;
