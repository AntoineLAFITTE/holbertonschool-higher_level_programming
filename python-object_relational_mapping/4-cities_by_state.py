#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa, along with
their state names.

The script takes three arguments:
1. MySQL username
2. MySQL password
3. Database name

Usage:
    ./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>

The script connects to a MySQL server running on localhost at port 3306
and retrieves all cities with their corresponding
 state names, sorted by cities.id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Capture command-line arguments
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

    # Execute the SQL query to join cities and states tables and retrieve data
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # Fetch all results and print them one by one
    for city in cursor.fetchall():
        print(city)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
