--  This script creates user user_0d_1 in the MySQL server
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
