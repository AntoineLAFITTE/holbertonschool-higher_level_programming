-- This script lists all records from the table second_table in the
-- specified database with a score of 10 or higher
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
