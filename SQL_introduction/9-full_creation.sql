-- This script creates a table named second_table with columns id (INT), name
-- (VARCHAR(256)), and score (INT) in the specified database.
-- If the table already exists, it will not be created again. The script also
-- inserts multiple rows into the table.
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);
