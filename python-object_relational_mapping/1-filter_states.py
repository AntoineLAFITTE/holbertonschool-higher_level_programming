#!/usr/bin/python3
"""
A script that lists all states with a name starting with 'N'
from the database hbtn_0e_0_usa.

The script takes three arguments:
1. MySQL username
2. MySQL password
3. Database name

Usage:
    ./1-filter_states.py <mysql_username> <mysql_password> <database_name>

The script connects to a MySQL server running on localhost at port 3306
and retrieves all states with names starting with 'N' (upper case) in
ascending order by states.id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Capture command-line arguments for username, password, and database name
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL database on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor to execute queries
    cursor = db.cursor()

    # Execute the SQL query to retrieve states with names starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all results and print them one by one
    for state in cursor.fetchall():
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
