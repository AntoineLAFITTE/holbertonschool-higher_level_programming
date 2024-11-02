#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa where
the name matches the user-provided argument.

The script takes four arguments:
1. MySQL username
2. MySQL password
3. Database name
4. State name to search for

Usage:
    ./2-my_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>

The script connects to a MySQL server running on localhost at port 3306
and retrieves states with a name matching the user input in ascending order by id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Capture command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

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

    # Execute the SQL query with user input using format to inject safely
    query = (
        "SELECT * FROM states "
        "WHERE name = '{}' "
        "ORDER BY id ASC"
    ).format(state_name_searched)
    cursor.execute(query)

    # Fetch all results and print them one by one
    for state in cursor.fetchall():
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
