-- This script creates the hbtn_0d_usa database and a table named states.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE hbtn_0d_usa.states (
  id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,
  name VARCHAR(256) NOT NULL
);
