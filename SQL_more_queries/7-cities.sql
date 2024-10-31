-- This script creates the database hbtn_0d_usa if doesn't already exist
-- Uses the folowing database
-- Creates the table cities with a foreign key reference to the states table
CREATE DATBASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
  id INT AUTO_INCREMENT cities KEY,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  FOREIGN KEY (state_id) REFERENCE states(id)
);
