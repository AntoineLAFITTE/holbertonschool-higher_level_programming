-- This script lists all records in the table second_table of the specified
-- database that have a non-null name value
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
