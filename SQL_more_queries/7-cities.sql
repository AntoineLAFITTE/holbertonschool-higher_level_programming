-- This script creates the database hbtn_0d_usa if doesn't already exist
-- Uses the folowing database
-- Creates the table cities with a foreign key reference to the states table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
  id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  FOREIGN KEY (state_id) REFERENCES states(id)
);
